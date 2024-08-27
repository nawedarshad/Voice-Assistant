import speech_recognition as sr
import commandProcess as cp
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()
re_check = True

def speak(text):
    engine.say(text)
    engine.runAndWait()
  
if __name__ == "__main__":
    speak("Initializing your personal Voice Assistant")

    print("Say something!")
    while re_check:
        try:
            with sr.Microphone() as source:
                audio = r.listen(source)
                command = r.recognize_google(audio)
                print(command)
                reply = cp.commandProcess(command)
                if reply == -1:
                    break
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Error; {0}".format(e))