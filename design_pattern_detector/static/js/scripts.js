document.getElementById('code-form').onsubmit = function(event) {
    event.preventDefault(); // Prevent default form submission
    const codeInput = document.getElementById('code-input').value;

    // Send code to the server via fetch
    fetch('/detect-patterns', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code: codeInput }),
    })
    .then(response => response.json())
    .then(data => {
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = ''; // Clear previous results

        // Populate results with detected patterns
        if (data.patterns.length > 0) {
            data.patterns.forEach(pattern => {
                const patternDiv = document.createElement('div');
                patternDiv.className = 'pattern';
                patternDiv.textContent = `${pattern.name}: ${pattern.description}`; // Display name and description
                resultsDiv.appendChild(patternDiv);
            });
        } else {
            resultsDiv.innerHTML = '<div class="pattern">No patterns detected.</div>';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
};
