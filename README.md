# Depression Recovery Project

This project aims to help individuals recover from depression through an automated system involving interaction with Alexa devices and ChatGPT. It records the user's feelings and notifies friends if there are concerns about their depression score.

## Project Structure

- `services/scheduler_service`: Service to schedule and initiate contact with the client on Alexa.
- `services/conversation_service`: Service to conduct GPT-generated conversations and assess the client using PHQ-9 and ALONE scales.
- `services/notification_service`: Service to notify friends or family if the client's score indicates a need for assistance.
- `services/database_service`: Service to store and retrieve client data and assessment scores.

## Running the Project

1. **Clone the repository:**

```bash
git clone git@github.com:pctjzer/bestie.git
cd depression_recovery_project
```

2. **Build and run the services using Docker Compose:**

```bash
docker-compose up --build
```

3. **Interacting with the services:**

   - Scheduler Service: [http://localhost:5001/schedule_contact](http://localhost:5001/schedule_contact)
   - Conversation Service: [http://localhost:5002/assess_client](http://localhost:5002/assess_client)
   - Notification Service: [http://localhost:5003/notify_contact](http://localhost:5003/notify_contact)
   - Database Service: [http://localhost:5004/store_data](http://localhost:5004/store_data)

## Future Enhancements

- Implement interaction with Alexa devices.
- Integrate ChatGPT for conversation handling.
- Add a scoring system to determine depression levels.
- Notify friends via different communication channels.
- Scale the services using Kubernetes.
- Deploy on a Raspberry Pi for smaller service offerings.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any improvements or suggestions.

## License

This project is open-source and available under the MIT License.
