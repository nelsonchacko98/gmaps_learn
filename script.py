import googlemaps
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

api_key = os.getenv("GOOGLE_MAPS_API_KEY")

# Initialize the Google Maps client with your API key
gmaps = googlemaps.Client(key=api_key)

def find_closest_location(current_location, locations):
    # Use Distance Matrix API to calculate the distance to each location
    distances = gmaps.distance_matrix(current_location, locations)
    
    # Extract the distance info
    elements = distances['rows'][0]['elements']
    
    # Find the index of the location with the shortest distance
    min_distance = float('inf')
    min_index = -1
    for i, element in enumerate(elements):
        if element['status'] == 'OK' and element['distance']['value'] < min_distance:
            min_distance = element['distance']['value']
            min_index = i
    
    return locations[min_index] if min_index >= 0 else None

# Example usage
current_location = "1600 Amphitheatre Parkway, Mountain View, CA"
locations = [
    "1 Infinite Loop, Cupertino, CA",
    "345 Spear St, San Francisco, CA",
    "1601 Willow Rd, Menlo Park, CA"
]

closest_location = find_closest_location(current_location, locations)
print(f"The closest location is: {closest_location}")
