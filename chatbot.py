import random

responses = {
    "hi": "Hello! How can I assist you today?",
    "how are you": "I'm just a bot, but I'm doing well. How about you?",
    "bye": "Goodbye! Have a great day!",
    "default": "Sorry, I didn't understand that. Can you ask something else?"
}

def chatbot():
    print("Bot: Hi, I'm your chatbot! Type 'bye' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "bye":
            print("Bot: Goodbye!")
            break
        
        response = responses.get(user_input, responses["default"])
        print(f"Bot: {response}")

if __name__ == "__main__":
    chatbot()
