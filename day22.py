import pyttsx3

def matalu_text(text):
    engine = pyttsx3.init()   
    engine.say(text)
    engine.runAndWait()
    engine.stop()

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Bot: Hello there!")
        matalu_text("Hello there!")

    elif user_input == "hi":
        print("Bot: Hi, how are you?")
        matalu_text("Hi, how are you?")

    elif user_input == "how are you":
        print("Bot: I am great, how are you doing?")
        matalu_text("I am great, how are you doing?")

    elif user_input == "im absolutely fine":
        print("Bot: Awesome buddy!")
        matalu_text("Awesome buddy!")

    elif user_input == "your name":
        print("Bot: I am a ChatBot.")
        matalu_text("I am a ChatBot.")

    elif user_input == "bye":
        print("Bot: Goodbye!")
        matalu_text("Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
        matalu_text("Sorry, I don't understand that.")
     
