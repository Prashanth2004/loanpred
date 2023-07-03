
import datetime
import os
from turtle import pd
from werkzeug.utils import secure_filename
from flask import Flask, jsonify, render_template, request, redirect, session, flash
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import mysql.connector

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'C:/Users/Abhiram/Desktop/MPP/models'
model = joblib.load('models/loan_model.pkl')
app.secret_key = 'your_secret_key'

# MySQL database configuration
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Prashu@2530',
    database='my_db'
)
def preprocess_data(married, dependents, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area):
    # Perform necessary preprocessing steps on the input data
    # ...
    # Example: Convert categorical variables to numerical representation
    married_mapping = {'No': 0, 'Yes': 1}
    education_mapping = {'Graduate': 0, 'Not Graduate': 1}
    self_employed_mapping = {'No': 0, 'Yes': 1}
    property_area_mapping = {'Rural': 0, 'Semiurban': 1, 'Urban': 2}

    married = married_mapping.get(married, 0)
    education = education_mapping.get(education, 0)
    self_employed = self_employed_mapping.get(self_employed, 0)
    property_area = property_area_mapping.get(property_area, 0)

    preprocessed_data = [married, dependents, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area,0]
    
    return np.array(preprocessed_data)

@app.route('/')
def page():
    return render_template('index.html')

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if user already exists
        cursor = db.cursor()
        
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        if user:
            return "User already exists. Please login or choose a different email."

        # Create new user
        current_date = datetime.date.today().strftime('%Y-%m-%d')
        cursor.execute("INSERT INTO users (username, email, password, date) VALUES (%s, %s, %s, %s)", (username, email, password, current_date))
        db.commit()
        return redirect('/login')
    return render_template('signup.html')

# Login route 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Validate user credentials
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        if user:
            session['user_id'] = user[0]
            return redirect('/application')
        else:
            return "Invalid email or password. Please try again."

    return render_template('login.html')

@app.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        if name != 'admin' or password != 'admin':
            return 'Invalid admin credentials'

        session['admin'] = True

        return redirect('/admin')

    return render_template('adminlogin.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

# Application form route
@app.route('/application', methods=['GET', 'POST'])
def application():
    # Check if user is logged in
    if 'user_id' in session:
        if request.method == 'POST':
            # Retrieve form data
            married = request.form['married']
            dependents = int(request.form['dependents'])
            education = request.form['education']
            self_employed = request.form['self_employed']
            applicant_income = float(request.form['applicant_income'])
            coapplicant_income = float(request.form['coapplicant_income'])
            loan_amount = float(request.form['loan_amount'])
            loan_amount_term = float(request.form['loan_amount_term'])
            credit_history = float(request.form['credit_history'])
            property_area = request.form['property_area']

            # Preprocess the form data
            preprocessed_data = preprocess_data(married, dependents, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area)

            # Make predictions using the loaded model
            prediction = model.predict([preprocessed_data])

            # Convert the prediction to a human-readable format
            if prediction[0] == 1:
                result = 'Approved'
            else:
                result = 'Not Approved' 

            # Store form data in the database
            cursor = db.cursor()
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute("INSERT INTO details (user_id, married, dependents, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area, result, entered_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (session['user_id'], married, dependents, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area, result, timestamp))
            db.commit()

            return render_template('form.html', result=result)

        return render_template('form.html')
    else:
        return redirect('/login')

@app.route('/history')
def history():
    # Check if user is logged in
    if 'user_id' in session:
        # Retrieve user's application history from the database
        cursor = db.cursor()
        cursor.execute("SELECT * FROM details WHERE user_id = %s", (session['user_id'],))
        history = cursor.fetchall()

        return render_template('history.html', history=history)
    else:
        return redirect('/login')

@app.route('/registrations')
def get_registrations():
    cursor = db.cursor()
    cursor.execute("SELECT date, COUNT(*) as count FROM users GROUP BY date")
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

# Route to retrieve prediction data from the database
@app.route('/predictions')
def get_predictions(): 
    cursor = db.cursor()
    cursor.execute("SELECT result, COUNT(*) as count FROM details GROUP BY result")
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)


# Logout route
@app.route('/logout')
def logout():
    # Clear session and redirect to login page
    session.pop('user_id', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
