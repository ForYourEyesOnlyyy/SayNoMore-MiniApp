from flask import Flask, render_template, request, jsonify
import os
import logging
from flask_cors import CORS

logging.basicConfig(level=logging.INFO)

app = Flask(__name__, template_folder="../templates", static_folder="../static")
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_trip():
    try:
        data = request.get_json()
        app.logger.info('Received data: %s', data)
        # Process the data as needed
        return jsonify({'status': 'success', 'message': 'Trip details received'})
    except Exception as e:
        app.logger.error('Error: %s', e)
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run()
