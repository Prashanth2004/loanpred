    const urlParams = new URLSearchParams(window.location.search);
    const result = urlParams.get('result');

    const resultContainer = document.getElementById('result-container');
    resultContainer.textContent = `Loan Approval Result: ${result}`;

