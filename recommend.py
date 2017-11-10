import argparse
from components import Location

parser = argparse.ArgumentParser(description='Recommend travel destination based on weather')
parser.add_argument('-weather', help='Your weather craving')
parser.add_argument('-max_distance', help='The max distance you wish to travel', default='100')

args = parser.parse_args()

locations = Location.find_destinations(args.max_distance)
nearby_cities = Location.extract_city_names(locations)

# TODO: Need to filter these cities based on weather preference

Location.list_cities(nearby_cities)
