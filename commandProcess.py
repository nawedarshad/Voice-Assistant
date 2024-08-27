import data
import speech_recognition as sr
import webbrowser
import pyttsx3
import pywhatkit as kit



r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def commandProcess(command):
    
    #hello
    for i in data.data["hello_list"]: 
        if i in command.lower():
            reply = "Hii, how can I help you?"
            print(reply)
            speak(reply)
            return 
    

    #Website
    for i in data.data["websites"]: 
        if i in command.lower():
            reply = f"Opening {i}"
            print(reply)
            speak(reply)
            webbrowser.open(f"https://{i}.com")
            return 
    
    
    #Search 
    if "search" in command.lower():
        reply = f"Searching..."
        print(reply)
        command = command.replace("search", "")
        speak(reply)
        webbrowser.open(f"https://www.google.com/search?q={command}")
        return 

    #browser
    for i in data.data["open_browser_phrases"]: 
        if i in command.lower():
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
        
    #song
    for i in data.data["play_song_phrases"]: 
        if i in command.lower():
            reply = "Tell me the Song name"
            print(reply)
            speak(reply)
            try:
                with sr.Microphone() as source:
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    # Play a song on YouTube
                    print(command)
                    kit.playonyt(command)
                    
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Error; {0}".format(e))
            return
        
    
    #goodbye 
    for i in data.data["bye_list"]: 
        if i in command.lower():
            reply = "Goodbye!!"
            print(reply)
            speak(reply)
            return -1
    
                
   