from gtts import gTTS
from playsound import playsound

comando = str(input("insira o comando"))
if comando == "tocar música": 
    tts = gTTS('Olá, eu sou Alexo', lang='pt')
tts.save('integracion.mp3')
playsound ("integracion.mp3")
