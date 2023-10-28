from flask import Flask, render_template, request
from util import generate_email

app = Flask(__name__)

# Create variables to store the email data, response instructions, and text
email_data = ""
response_instructions = ""
reply = False

@app.route('/', methods=['GET', 'POST'])
def process_form():
    global email_data, response_instructions, text

    text = ''

    if request.method == 'POST':
        email_data = request.form['email_data']
        response_instructions = request.form['response_instructions']
        reply = request.form.get('reply') == 'reply'
        text = generate_email(email_data, response_instructions, reply)

    return render_template('index.html', text=text)  # Pass the 'text' variable to the template

if __name__ == '__main__':
    app.run(debug=True)
