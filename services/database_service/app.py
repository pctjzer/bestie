from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
database = {
    'clients': [],
    'assessments': []
}

@app.route('/store_data', methods=['POST'])
def store_data():
    data = request.json
    database['assessments'].append(data)
    return jsonify({'status': 'Data stored', 'data': data})

@app.route('/retrieve_data', methods=['GET'])
def retrieve_data():
    return jsonify({'status': 'Data retrieved', 'data': database})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
