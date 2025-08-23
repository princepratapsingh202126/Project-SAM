import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Set the timeout duration in seconds
timeout = 10

# Capture microphone input
with sr.Microphone() as source:
    print("Speak something...")
    try:
        audio = r.listen(source, timeout=timeout)
    except sr.WaitTimeoutError:
        print("Timeout occurred. No speech detected.")
        exit()

try:
    # Use Google Speech Recognition
    text = r.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Speech recognition could not understand audio.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
