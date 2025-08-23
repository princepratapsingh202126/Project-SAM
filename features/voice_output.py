import pyttsx3

def say(text):
    engine = pyttsx3.init()
    print(text)
    engine.say(text)
    engine.runAndWait()