// JavaScript to conditionally show/hide the email_data textarea
// main.js
document.addEventListener('DOMContentLoaded', function () {
    const replySelect = document.getElementById('reply');
    const emailDataGroup = document.getElementById('email-data-group');
    const emailDataTextarea = document.getElementById('email_data');

    replySelect.addEventListener('change', () => {
        if (replySelect.value === 'reply') {
            emailDataGroup.style.display = 'block';
            emailDataTextarea.required = true;
        } else {
            emailDataGroup.style.display = 'none';
            emailDataTextarea.required = false;
        }
    });
});
