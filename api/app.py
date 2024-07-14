from flask import Flask, render_template, request, jsonify
import os
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    print(f"Received form data: {data}")  # Log the data for debugging purposes
    return jsonify({'status': 'success', 'message': 'Form submitted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
