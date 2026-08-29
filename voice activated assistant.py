import webbrowser
import datetime
import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate',160)
    print("Assistant",text)
    engine.say(text)
    engine.runAndWait()

def reco():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print("Listening...")
        r.adjust_for_ambient_noise(src,duration =0.5)
        try:
            audio = r.listen(src,timeout =8)

        except sr.WaitTimeoutError:
            print("Time out, Try again!")
            return " "
    try:
        command = r.recognize_google(audio)
        print("You ", command)
        return command.lower()
    except:
        print("Not Able to hear you")
        return " "

def respond1(command):
   

    if('name' in command):
        print("My name is Jarvis")
        speak("My name is Jarvis")

    elif('open google' in command):
        print("oppening google...")
        speak("oppening google...")
        webbrowser.open('https://www.google.com')

    elif('open youtube' in command):
        print("Opening youtube...")
        speak("opening youtube...")
        webbrowser.open('https://www.youtube.com')
    elif('exit' in command or 'stop' in command):
        print("Exitiong...")
        speak("Goodbye")
        return False

    else:
        print("Not able to hear you")
    return True

def main():
    print("welcome to voice assistant")

    while True:
        command = reco()
        if command and not respond1(command):
            break
main()
