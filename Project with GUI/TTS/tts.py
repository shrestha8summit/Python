# install pyttsx3 library using pip
import tkinter as tk
import pyttsx3 
from tkinter import StringVar, E, W, N, S

app = tk.Tk()
app.geometry("400x450")
app.config(background="purple")
app.title("Test to speech")

ipText = StringVar()

header = tk.Label(app,text="CONVERT  TEXT  I/P  TO   AUDIO  O/P:",bg="purple",fg="black",font=("Impact",15,"bold"))
header.grid(padx=(45,0),pady=(80,0))

ipLabel = tk.Label(app,text="Enter the text : ",font=("Times",15,"italic"),bg="purple",fg="white",)
ipLabel.grid(row=3,padx=(70,0),pady=(50,10))


ipEntry = tk.Entry(app,textvariable=ipText)
ipEntry.grid(padx=(50,0),pady=(10,0))


def convert():
     text_speech = pyttsx3.init()
     text_speech.say(ipText.get())
     text_speech.runAndWait()


convertBtn = tk.Button(app,text="Convert",bg="blue",fg="gold",bd=5,cursor="hand2",font=("Times",15,"italic"),command=convert)
convertBtn.grid(sticky=W,padx=(160,0),pady=(50,0))

clsBtn = tk.Button(app,text=" Close ",bg="black",fg="red",bd=5,cursor="hand2",font=("Times",15,"italic"),command=app.destroy)
clsBtn.grid(sticky=W,padx=(163,0),pady=(20,0))

app.mainloop()