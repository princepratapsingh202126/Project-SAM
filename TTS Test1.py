import pyttsx3

engine = pyttsx3.init()

def say(text):
    # Setting Rate and Volume 
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 2)

    #Say the test
    engine.say(text)
    engine.runAndWait()


say("Hello World")
