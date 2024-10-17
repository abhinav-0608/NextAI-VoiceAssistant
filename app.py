from flask import Flask, request, jsonify

app = Flask(__name__)

# Root URL to confirm the server is running
@app.route('/')
def index():
    return "Flask server is running"

# Webhook URL for Dialogflow
@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the request JSON from Dialogflow
    req = request.get_json(silent=True, force=True)

    # Extract parameters from the JSON
    intent = req.get('queryResult').get('intent').get('displayName')
    parameters = req.get('queryResult').get('parameters')

    if intent == 'Add Event':  # Make sure this matches your Dialogflow intent name
        date_time = parameters.get('date-time')
        event_title = parameters.get('event-title')

        # Process the date and event_title, perhaps adding it to Google Calendar
        response_text = f"Event '{event_title}' scheduled for {date_time}."

        # Return a response back to Dialogflow
        return jsonify({
            "fulfillmentText": response_text
        })

    return jsonify({
        "fulfillmentText": "Sorry, I didn't understand that."
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
