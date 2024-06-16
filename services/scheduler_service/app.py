from flask import Flask, request, jsonify
import schedule
import time
import threading

app = Flask(__name__)

# Function to be scheduled
def contact_client():
    # Logic to initiate contact with Alexa device
    print("Contacting client via Alexa...")

# Route to schedule contact
@app.route('/schedule_contact', methods=['POST'])
def schedule_contact():
    data = request.json
    # Schedule the contact (for demo purposes, every 10 seconds)
    schedule.every(10).seconds.do(contact_client)
    return jsonify({'status': 'Contact scheduled', 'data': data})

# Run scheduled tasks
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()
    app.run(host='0.0.0.0', port=5001)
