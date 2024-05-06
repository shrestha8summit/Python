# install pyttsx3 library using pip

import pyttsx3 
text_speech = pyttsx3.init()
answer = input("What do you want to convert into speech:\t")
text_speech.say(answer)
text_speech.runAndWait()