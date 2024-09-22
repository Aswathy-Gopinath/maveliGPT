from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Predefined responses
responses = {
    "who is maveli": "Maveli, also known as Mahabali, is a mythical king celebrated during the Onam festival in Kerala.",
    "what is onam": "Onam is a harvest festival celebrated in Kerala, marking the return of King Mahabali.",
    "when is onam": "Onam is celebrated in the month of Chingam (August-September), with the main festivities lasting for ten days.",
    "how is onam celebrated": "Onam is celebrated with feasts, traditional games, floral decorations, and various cultural events.",
    "tell me about onam traditions": "Traditions include making 'pookalam' (flower carpets), preparing the Onam Sadhya (feast), and conducting various cultural performances.",
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input'].lower()
    response = responses.get(user_input, "I’m sorry, I don't understand that. Can you ask something else about Maveli or Onam?")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
