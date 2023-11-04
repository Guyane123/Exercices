import http.client
import json

APIKEY = "4339a532a86b4eb800539bc7d239a0ad"
API_HOST = "api.openweathermap.org"

class weather:
    def __init__(self, location, currentWeather, windSpeed):
        self.location = location
        self.currentWeather = currentWeather
        self.windSpeed = windSpeed * 3.6


def getWeather(LOCATION) :

    API_PATH = f"/data/2.5/weather?q={LOCATION}&units=metric&appid={APIKEY}"
    
    try:
        # Establish a connection to the API host
        connection = http.client.HTTPSConnection(API_HOST)

        # Send a GET request
        connection.request("GET", API_PATH)

        # Get the response
        response = connection.getresponse()

        if response.status == 200:
            data = response.read()

            json_string = data.decode("utf-8")

            json_data = json.loads(json_string)

            
            return weather(json_data["name"], json_data["weather"][0]["main"], json_data["wind"]["speed"])
        else:
            print(f"Failed to fetch data. Status code: {response.status}")
            return weather("Hennebont", "Rain", "error")
    except Exception as e:
        print(f"An error occurred: {e}")

