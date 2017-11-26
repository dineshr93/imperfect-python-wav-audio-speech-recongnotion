import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.AudioFile("in.wav") as source:
    audio = recognizer.record(source)
try:
    text = recognizer.recognize_google(audio)
    print(text)
except Exception as e:
    print("Exception: "+str(e))