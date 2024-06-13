import os
from dotenv import load_dotenv
import requests

load_dotenv()

key = os.getenv("key")
api_key = key


city = input("Enter city: ")
print(city)

request =  requests.get(f"  https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

weather= request.json()['weather'][0]['main'] 
temp = round(request.json()['main']['temp'] )

print(f"{request.json()}")
print (f"Weather in {city} is: {weather}")
print (f"The temperature in {city} is : {temp} Fahrenheit")