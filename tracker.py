import requests

# Enter your API key here
api_key = "LGvIjmiwjPkWC1A0TtZ9krjGcghKJ3lI"

# Enter the latitude and longitude of the location you want to track Typhoon weather for
lat = "35.6895"
lon = "139.6917"

# Create the API endpoint URL
url = f"https://api.tomorrow.io/v4/timelines?location={lat},{lon}&fields=weather&timesteps=1d&apikey={api_key}"

# Send the HTTP request to the API endpoint
response = requests.get(url)

# Parse the JSON response
weather_data = response.json()

# Get the weather conditions for tomorrow
tomorrow_weather = weather_data["data"]["timelines"][0]["intervals"][1]["values"]["weather"]

# Get the wind speed for tomorrow
tomorrow_wind_speed = weather_data["data"]["timelines"][0]["intervals"][1]["values"]["wind_speed"]

# Check if there is a typhoon warning in effect
if "typhoon" in tomorrow_weather.lower() or tomorrow_wind_speed >= 15:
    print("There is a Typhoon warning in effect for tomorrow.")
else:
    print("There is no Typhoon warning in effect for tomorrow.")
    