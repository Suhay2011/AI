import speech_recognition as sr
from googletrans import Translator

def speech_to_text():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak in English...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="en-US")
        print("You Said: ", text)
        return text
    except:
        print("Could not understand.")
        return ""

def translate_text(text):
    translator = Translator()
    result = translator.translate(text, src="en", dest="fr")
    print("french:", result.text)

text = speech_to_text()

if text:
    translate_text(text)
