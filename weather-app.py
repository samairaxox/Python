import pyttsx3
import requests

# Initialize text-to-speech engine
x = pyttsx3.init()

print("Welcome to the Weather App:")

while True:
    location = input("Enter location (Enter 0 to exit): ")

    if location == "0":
        print("Exited the program")
        x.say("Exited the program")
        x.runAndWait()
        break
    else:
        location = location.strip()  # FIXED: Reassign the stripped value

        # Replace this with your own API key
        API_key = '3357c8431bb636571e4f9e2fc8f2e2c9'

        # Use the location input by the user
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_key}&units=metric"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_desc = data['weather'][0]['description']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']

            print(f"Weather is : {weather_desc}")
            print(f"Current Temperature is : {temp}°C")
            print(f"Current Temperature Feels like : {feels_like}°C")
            print(f"Humidity is : {humidity}%")

            # Speaking
            x.say(f"The weather in {location} is {weather_desc}")
            x.say(f"The current temperature is {temp} degrees Celsius")
            x.say(f"It feels like {feels_like} degrees")
            x.say(f"The humidity is {humidity} percent")
            x.runAndWait()
        else:
            print("Failed to get weather data. Please check the city name.")
            x.say("Failed to get weather data. Please check the city name.")
            x.runAndWait()

