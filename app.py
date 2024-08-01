from flask import Flask, request, render_template, jsonify
from pprint import pprint as pp

# Create Flask app
app = Flask(__name__)

conversation = [
    {"role": "ai", "msg": "Hi there!<br>How can I help you today?"},
    {"role": "human", "msg": "How are you?"},
    {"role": "ai", "msg": "I'm doing fine.<br>Thanks for asking!"},
    {"role": "human", "msg": "What is your name?"},
    {
        "error": True,
        "role": "ai",
        "msg": "Oops!<br>Something went wrong.<br>Please try again.",
    },
]


# Define route for home page
@app.route("/")
def main():
    return render_template("index.html", data=conversation)


# Define route for test page
@app.route("/process-data", methods=["POST"])
def process_data():
    data = request
    text = request.get_data(as_text=True)
    print(text)
    user_msg = data.json["msg"]
    conversation.append(data)
    # Get the LLM response for the given input and context 
    response = "Bot answer."
    conversation.append({"role": "ai", "msg": response})
    return jsonify({"msg": response})


if __name__ == "__main__":
    app.run(debug=True)
