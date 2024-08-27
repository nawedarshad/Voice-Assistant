import speech_recognition as sr
import webbrowser
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()
re_check = True
data = {
    "hello_list": [
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
],
    "bye_list": [
    "bye",
    "goodbye",
    "see you",
    "later",
    "farewell",
    "take care",
    "see ya",
    "bye-bye",
    "good night",
]

}


def speak(text):
    engine.say(text)
    engine.runAndWait()

def commandProcess(command):
     for i in data["hello_list"]: 
        if command.lower() == i:
            reply = "Hii, how can I help you?"
            print(reply)
            speak(reply)
            return 
     for i in data["bye_list"]: 
        if command.lower() == i:
            reply = "Goodbye!!"
            print(reply)
            speak(reply)
            global re_check
            re_check = False
                
     

if __name__ == "__main__":
    speak("Initializing your personal Voice Assistant")

    print("Say something!")
    while re_check:
        try:
            with sr.Microphone() as source:
                audio = r.listen(source)
                command = r.recognize_google(audio)
                print(command)
                commandProcess(command)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Error; {0}".format(e))