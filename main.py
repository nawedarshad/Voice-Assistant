import speech_recognition as sr
import webbrowser
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing your personal Voice Assistant")
    hello_list = [
    "hi",
    "hello",
    "hey",
    "greetings",
    "howdy",
    "hiya",
    "what's up",
    "sup",
    "yo",
    "good day",
    "hey there",
    "bonjour",   # French for hello
    "hola",      # Spanish for hello
    "salutations",
    "namaste",   # Hindi greeting
    "ahoy",
    "aloha",     # Hawaiian greeting
    "ciao",      # Italian for hello/goodbye
    "shalom",    # Hebrew for peace/hello
    "salaam",    # Arabic for peace/hello
    "wassup",
    "morning",   # Short for good morning
    "evening",   # Short for good evening
    "yo yo",
    "hey yo"
]

    while True:
        try:
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                for i in hello_list: 
                    if command.lower() == i:
                     reply = "Hii, how can I help you?"
                     print(reply)
                     speak(reply)
                if command.lower() == "bye":
                     speak("Goodbye")
                     break
        except sr.UnknownValueError:
                print("Could not understand audio")
        except sr.RequestError as e:
                print("Error; {0}".format(e))