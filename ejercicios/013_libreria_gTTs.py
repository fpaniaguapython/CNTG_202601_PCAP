# pip install gTTS

from gtts import gTTS

import os

fichero = open('receta.txt',mode='rt',encoding='utf-8')
texto = fichero.read()
fichero.close()

language = 'es'

myobj = gTTS(text=texto, lang=language, slow=False)

myobj.save("welcome.mp3")

os.system("start welcome.mp3")