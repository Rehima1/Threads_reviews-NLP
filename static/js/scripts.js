function submitForm() {
    const form = document.getElementById('reviewForm');
    const formData = new FormData(form);

    fetch('/analyze', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            const outputDiv = document.getElementById('output');
            outputDiv.style.display = 'block';
            outputDiv.innerHTML = `
                <strong>Sentiment:</strong> ${data.sentiment}<br>
                <strong>Source:</strong> ${data.source}<br>
                <strong>Rating:</strong> ${data.rating} stars<br>
                <strong>Review Description:</strong> ${data.review_description}<br>
            `;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while processing your request.');
    });
}
