import speech_recognition as sr
import webbrowser
import pyttsx3
import data

r = sr.Recognizer()
engine = pyttsx3.init()
re_check = True

def speak(text):
    engine.say(text)
    engine.runAndWait()

def commandProcess(command):
     
    for i in data.data["hello_list"]: 
        if command.lower() == i:
            reply = "Hii, how can I help you?"
            print(reply)
            speak(reply)
            return 
    
    for i in data.data["websites"]: 
        a = "open " + i
        if command.lower() == a:
            reply = f"Opening {i}"
            print(reply)
            speak(reply)
            webbrowser.open(f"https://{i}.com")
            return 


    for i in data.data["open_browser_phrases"]: 
        if command.lower() == i:
            reply = "Tell me the Domain name"
            print(reply)
            speak(reply)
            try:
                with sr.Microphone() as source:
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f"Opening URL: {command}")
                    webbrowser.open(f"https://{command}")
                    
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Error; {0}".format(e))
            return
        
     
    for i in data.data["bye_list"]: 
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