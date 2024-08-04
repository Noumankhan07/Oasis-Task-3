import requests

def get_weather(api_key, location):
    """Fetch weather data from OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data. Please check the location and API key.")
        return None

def display_weather(data):
    """Display weather information."""
    if data:
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        conditions = data['weather'][0]['description']

        print(f"\nWeather in {city}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {conditions.capitalize()}")
    else:
        print("No data to display.")

def main():
    print("Welcome to the Command-line Weather App!")
    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    location = input("Enter a city or ZIP code: ").strip()

    weather_data = get_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
