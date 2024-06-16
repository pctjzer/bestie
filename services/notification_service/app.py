from flask import Flask, request, jsonify

app = Flask.__name__)

@app.route('/notify_contact', methods=['POST'])
def notify_contact():
    data = request.json
    # Logic to notify contacts
    return jsonify({'status': 'Contact notified', 'data': data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
