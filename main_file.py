from flask import Flask, render_template, request
from chat_bot_file import handle_query
from flask import jsonify

app = Flask(__name__)

# Function to get chatbot response
def get_bot_response(user_message):
    return f"Bot: {handle_query(user_message)}"
@app.route('/')
def chat():
    return render_template('template_file.html')

@app.route('/get', methods=['POST'])
def get_response():
    user_message = request.form['msg']
    bot_response = get_bot_response(user_message)
    return bot_response
if __name__ == '__main__':
    app.run(debug=True)
