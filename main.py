from flask import Flask, request, jsonify
from lawyerAI import get_response  # Ensure you have a function to handle responses

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    language = data.get('language', 'en')  # Handle multiple languages if needed
    response = get_response(user_message, language)
    return jsonify({'ai_explanation': response})

if __name__ == '__main__':
    app.run(debug=True)
