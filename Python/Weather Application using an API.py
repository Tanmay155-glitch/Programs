import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if data['cod'] == 200:
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"Temperature in {city}: {temp}°C")
        print(f"Weather description: {description}")
    else:
        print("City not found.")

def main():
    api_key = input("Enter your API key: ")
    city = input("Enter city name: ")
    get_weather(api_key, city)

if __name__ == "__main__":
    main()
