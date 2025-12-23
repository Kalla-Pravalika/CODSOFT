def chatbot():
    print("Chatbot: Hello! I am a rule-based chatbot 🤖")
    print("Chatbot: You can talk to me. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! Nice to meet you 😊")

        elif "name" in user_input:
            print("Chatbot: I am a simple rule-based chatbot created using Python.")

        elif "how are you" in user_input:
            print("Chatbot: I'm doing great! Thanks for asking.")

        elif "what can you do" in user_input:
            print("Chatbot: I can chat with you, answer simple questions, and keep you company.")

        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}")

        elif "date" in user_input:
            from datetime import datetime
            current_date = datetime.now().strftime("%d-%m-%Y")
            print(f"Chatbot: Today's date is {current_date}")

        elif "help" in user_input:
            print("Chatbot: You can ask me about my name, time, date, or just say hello.")

        elif "thank" in user_input:
            print("Chatbot: You're welcome! 😊")

        elif "who created you" in user_input:
            print("Chatbot: I was created as part of an AI internship project at CODSOFT.")

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day 👋")
            break

        else:
            print("Chatbot: Sorry, I didn't understand that. Can you try again?")


chatbot()


