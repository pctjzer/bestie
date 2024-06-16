from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/assess_client', methods=['POST'])
def assess_client():
    data = request.json
    # Logic to conduct conversation and assess using PHQ-9 and ALONE scales
    return jsonify({'status': 'Client assessed', 'data': data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
