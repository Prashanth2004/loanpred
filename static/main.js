function validateForm() {
    var name = document.getElementById("name");
    var email = document.getElementById("email");
    var password = document.getElementById("password");

    // Check if name is empty
    if (name.value.trim() === "") {
        alert("Please enter your name.");
        name.focus();
        return false;
    }

        // Check if email is empty
    if (email.value.trim() === "") {
        alert("Please enter your email.");
        email.focus();
        return false;
    }

    // Check if email is valid
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email.value.trim())) {
        alert("Please enter a valid email address.");
        email.focus();
        return false;
    }

    // Check if password is empty
    if (password.value.trim() === "") {
        alert("Please enter your password.");
        password.focus();
        return false;
    }

    // Add additional validation logic if needed

    return true;
}
