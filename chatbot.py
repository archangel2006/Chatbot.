import google.generativeai as genai

# Set your Gemini API key
API_KEY = "API_Key"
genai.configure(api_key=API_KEY)

# Use a model that exists in your list
model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Change model here

chat = model.start_chat()

print("Welcome to Chatbot!")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = chat.send_message(user_input)
    print("Chatbot:", response.text)
