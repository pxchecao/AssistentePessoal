#declarou as bibliotecas
from gtts import gTTS
from playsound import playsound

#reproduziu a fala
tts = gTTS('Olá, eu sou Alexo', lang='pt')
tts.save('integracion.mp3')
playsound ("integracion.mp3")