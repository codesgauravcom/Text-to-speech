from gtts import gTTS
from playsound import playsound

audio= 'speech.mp3'
language= 'en'
sp= gTTS(text = 'hello from codesgaurav ', lang= 'en', slow= False)

sp.save(audio)
playsound(audio)
