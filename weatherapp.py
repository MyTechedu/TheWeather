import requests

API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxx" 

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Please Enter a City Name: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    
    print("................................................")
    weather_data = data['weather'][0]['description'] # Using key to access value
    temperature_data = round(data['main']['temp'] - 273.15,2) # Using keys 'main' & 'temp' to access values
    print(f"The Weather of {city} : {weather_data}")
    print(f"The Temperature of {city} : {temperature_data} Degree Celsius ")
    print("................................................")
    
    
    
else:
    print("An error occurred.")