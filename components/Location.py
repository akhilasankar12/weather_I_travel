import requests

def find_destinations(radius):
	response = requests.get("http://getnearbycities.geobytes.com/GetNearbyCities?&radius="+radius)
	return response.json()


def extract_city_names(locations):
	return [", ".join((location[1], location[2], location[3])) for location in locations]


def list_cities(cities):
	for city in cities:
		print city