import speech_recognition as sr

# Initialize recognizer object
r = sr.Recognizer()

# Set the language model file for PocketSphinx
r.energy_threshold = 4000
r.dynamic_energy_threshold = True
r.dynamic_energy_adjustment_ratio = 2.5
r.pause_threshold = 0.5
r.operation_timeout = 5
r.phrase_threshold = 0.3

# Capture microphone input
with sr.Microphone() as source:
    print("Speak something...")
    try:
        audio = r.listen(source)

        # Recognize speech using PocketSphinx
        text = r.recognize_sphinx(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Speech Recognition service:", e)
