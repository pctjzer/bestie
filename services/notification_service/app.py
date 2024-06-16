from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = 'YOUR_OPENAI_API_KEY'

# Function to notify contact
def notify_contact(contact, summary):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Notify contact about client needs...\n\nContact: {contact}\nSummary: {summary}",
        max_tokens=150
    )
    notification_message = response.choices[0].text
    # Placeholder for actual notification logic
    print(notification_message)

@app.route('/notify_contact', methods=['POST'])
def notify_contact_route():
    data = request.json
    contact = data.get('contact')
    summary = data.get('summary')
    notify_contact(contact, summary)
    return jsonify({'status': 'Contact notified', 'data': data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
