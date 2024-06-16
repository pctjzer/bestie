from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/schedule_contact', methods=['POST'])
def schedule_contact():
    data = request.json
    # Logic to schedule contact on Alexa
    return jsonify({'status': 'Contact scheduled', 'data': data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
