import nltk
from nltk.chat.util import Chat, reflections

# Define a list of pairs for pattern-response
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! What can I help you with?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to assist you. You can call me ChatBot!"]
    ],
    [
        r"how are you?",
        ["I'm just a bot, but I'm here to help! How about you?", "I'm functioning as expected! What about you?"]
    ],
    [
        r"what can you do?",
        ["I can answer your questions and help with simple tasks. Try asking me something!"]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "Glad I could help!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day!", "See you soon!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that. Could you rephrase?"]
    ],
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

def chatbot_interface():
    print("ChatBot: Hi! I am your assistant. Type 'bye' to exit the chat.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chatbot_interface()
