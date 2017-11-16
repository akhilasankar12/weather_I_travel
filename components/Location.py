import requests

def find_destinations(radius):
	response = requests.get("http://getnearbycities.geobytes.com/GetNearbyCities?&radius="+radius)
	return response.json()


def extract_city_names(locations):
	return [", ".join((location[1], location[2], location[3])) for location in locations]


def list_cities(cities):
	for city in cities:
		print city + ": " + getWeather(city)


def getWeather(city):
	cityName = city.split(", ")[0]
	response = requests.get("https://www.metaweather.com/api/location/search?query="+ cityName)
	responseJson = response.json()
	if (len(responseJson) > 0):
		woeid = responseJson[0]["woeid"]
		weatherData = requests.get("https://www.metaweather.com/api/location/"+str(woeid)).json()
		weather = weatherData["consolidated_weather"][0]["weather_state_name"]
		return weather
	else:
		return "No data found"