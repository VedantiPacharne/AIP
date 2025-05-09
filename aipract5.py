import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required resources once
nltk.download('punkt')
nltk.download('stopwords')

def preprocess(user_input):
    tokens = word_tokenize(user_input.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in tokens if word.isalnum() and word not in stop_words]
    return filtered_words

def add_link(text, url):
    return f"{text} Visit: {url}"

def bookstore_chatbot_nlp():
    print("Welcome to SmartBook Store!")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Bot: Thank you! Have a great day!")
            break

        words = preprocess(user_input)

        if any(word in words for word in ["hi", "hello", "hey"]):
            print("Bot: Hello! How can I help you today?")
        elif any(word in words for word in ["hour", "time", "open", "timing"]):
            print("Bot: We're open from 9 AM to 9 PM, Monday to Saturday.")
        elif any(word in words for word in ["harry", "potter"]):
            print("Bot: Yes, 'Harry Potter' is available!")
        elif any(word in words for word in ["ebook", "digital"]):
            response = add_link("Yes, we offer eBooks on our website.", "https://www.smartbook.com/ebooks")
            print(f"Bot: {response}")
        elif "return" in words:
            print("Bot: You can return a book within 7 days with the receipt.")
        elif "order" in words and "status" in words:
            print("Bot: Please provide your order ID to check the status.")
        elif any(word in words for word in ["contact", "phone", "call"]):
            response = add_link("Call us at +1-555-BOOKS or email support@smartbook.com.", "https://www.smartbook.com/contact")
            print(f"Bot: {response}")
        elif any(word in words for word in ["location", "address", "where"]):
            print("Bot: We're located at 123 Book Street, NYC.")
        elif "membership" in words:
            response = add_link("Join our membership for 10% off and special offers.", "https://www.smartbook.com/membership")
            print(f"Bot: {response}")
        else:
            print("Bot: Sorry, I didn't understand that. Can you rephrase?")

# Run the chatbot
bookstore_chatbot_nlp()
