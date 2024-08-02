from flask import Flask, request, render_template, jsonify
from chatbot import get_response
from utils import HISTORY, ERROR_MSG

# Start the conversation with the provided history
conversation = HISTORY

# Create Flask app
app = Flask(__name__)


# Define route for home page
@app.route("/")
def main():
    return render_template("index.html", data=conversation)


# Define route for data processing
@app.route("/process-data", methods=["POST"])
def process_data():
    # Get the data from the request
    data = request
    text = request.get_data(as_text=True)
    user_msg = data.json["msg"]
    # Get the LLM response for the given input message and conversation context
    response = get_response(conversation, user_msg)
    # Append the user and chatbot prompt to the conversation context
    conversation.append(text)
    if response == ERROR_MSG:
        result = {"error": True, "role": "ai", "msg": response}
    else:
        result = {"role": "ai", "msg": response}
    conversation.append(result)
    return jsonify(result)


if __name__ == "__main__":
    # Run Flask app
    app.run(debug=True)
