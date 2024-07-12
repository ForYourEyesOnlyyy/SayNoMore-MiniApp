from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    # Log the received data for now
    print(data)
    return jsonify({'status': 'success', 'message': 'Form submitted and sent to Telegram!'})

if __name__ == '__main__':
    app.run(debug=True)