import requests

api_key = "df58e4eca5e8083a7809d50d6b89c0e4"


city = input("Enter city: ")
print(city)

request =  requests.get(f"  https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

weather= request.json()['weather'][0]['main'] 
temp = round(request.json()['main']['temp'])

print (f"Weather in {city} is: {weather}")
print (f"The temperature in {city} is : {temp} Fahrenheit")