from gtts import gTTS
from playsound import playsound

text = "Ok Done"
# text = input("Enter your text: ")

tts = gTTS(text)
tts.save("hi.mp3")

playsound('hi.mp3')
