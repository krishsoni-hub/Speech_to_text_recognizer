import speech_recognition as sr

# create recognizer object
r = sr.Recognizer()

# use microphone as source
with sr.Microphone() as source:
    print("Speak something...")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    # convert speech to text using Google API
    text = r.recognize_google(audio)
    print("You said:", text)

except sr.UnknownValueError:
    print("Sorry, could not understand audio")

except sr.RequestError:
    print("Network error")