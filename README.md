# ghw-api-tracker

## Here's how the Typhoon tracker works:

* Sign up for a free API key from tomorrow.io and replace "YOUR_API_KEY" with your own API key in the code.
* Enter the latitude and longitude of the location you want to track Typhoon weather for in the "lat" and "lon" variables, respectively.
* The code creates the API endpoint URL using the location and API key, and specifies that we want to get weather data for tomorrow ("timesteps=1d").
* The code sends an HTTP request to the API endpoint and gets a JSON response.
* The code parses the JSON response to get the weather conditions and wind speed for tomorrow.
* The code checks if there is a typhoon warning in effect by checking if the word "typhoon" is in the weather conditions or if the wind speed is greater than or equal to 15 meters per second (which is the threshold for a typhoon warning in Japan).
* The code prints out whether there is a Typhoon warning in effect or not for tomorrow.
* You can customize this code to fit your needs, such as adding more locations to track, changing the threshold for a typhoon warning, or adding more weather data to display.

