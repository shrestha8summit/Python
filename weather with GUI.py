import os
import tkinter as tk
import requests
from tkinter import StringVar ,W 
from dotenv import load_dotenv

load_dotenv()



app = tk.Tk()

app.geometry("900x450")
app.config(background="orange")

app.title("Weather forecast app")

def search():
        opLbl.config(text="City name : "+city.get())
        key = os.getenv("key")
        api_key = key
        request =  requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city.get()}&units=imperial&APPID={api_key}")
        
        weather = request.json()['weather'][0]['main']
        temp    = round(request.json()['main']['temp'])

        if request.status_code == 200 :
                opLbl1.config(text=f"Weather     : {weather}")
                opLbl2.config(text=f"Temperature : {temp}°F")
        else:
                opLbl1.config(text="Weather     : NA")
                opLbl2.config(text="Temperature : NA")

lbl1 = tk.Label(app,text="This application will help you to find weather and temperature of any specific city :",font=("Helveticaw Roman",15,"bold"))
lbl1.grid(padx=(50,0),pady=(50,0))

lbl2 = tk.Label(app,text="Enter the name of the city :",fg="purple",bg="orange",font=("Arial",15,"bold"))
lbl2.grid(padx=(50,0),pady=(50,0))

city = tk.StringVar()

entr =  tk.Entry(app,textvariable=city)
entr.grid(padx=(0,0),pady=(15,0))

oprBtn = tk.Button(app,text="Search",font=("Silkscreen",15),fg="green",bg="black",bd=5,cursor="hand2",command=search,justify="left")
oprBtn.grid(row=5,pady=(50,0),sticky=W,padx=(300,0))

clsBtn = tk.Button(app,text="Close",font=("Silkscreen",15),fg="red",bg="black",bd=5, cursor="hand2",command=app.destroy,justify="right")
clsBtn.grid(row=5,padx=(150,0),pady=(50,0))


opLbl = tk.Label(app,bg="orange",fg="brown",font=("Times New Roman",14),justify="center")
opLbl.grid(sticky=W,padx=(325,0),pady=(40,0))

opLbl1 = tk.Label(app,bg="orange",fg="brown",font=("Times New Roman",14),justify="center")
opLbl1.grid(sticky=W,padx=(325,0),pady=(5,0))

opLbl2 = tk.Label(app,bg="orange",fg="brown",font=("Times New Roman",14),justify="center")
opLbl2.grid(sticky=W,padx=(325,0),pady=(5,0))

app.mainloop()