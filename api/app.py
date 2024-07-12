from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    user_id = data['userId']
    message = f"New trip planned by user {user_id}:\n" \
              f"Departure: {data['departure']}\n" \
              f"Destination: {data['destination']}\n" \
              f"Arrival Date: {data['arrival']}\n" \
              f"Return Date: {data['return']}\n" \
              f"Budget: {data.get('budget', 'Not specified')}"

    response = requests.post(
        f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage',
        data={'chat_id': user_id, 'text': message}
    )

    if response.status_code == 200:
        return jsonify({'status': 'success', 'message': 'Form submitted and sent to Telegram!'})
    else:
        return jsonify({'status': 'error', 'message': 'Failed to send message to Telegram!'}), 500

if __name__ == '__main__':
    app.run(debug=True)