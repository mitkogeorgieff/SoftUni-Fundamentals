import re
pattern = r"([\/=])([A-Z][a-zA-z]{2,})\1"
places = input()

# Use the regular expression pattern to find all valid travel destinations in the input string
valid_places = re.findall(pattern, places)

# Calculate the total number of travel points and create a list of all valid travel destinations
travel_points = 0
destinations = []
for current_place in valid_places:
    # Add the length of the current destination name to the total number of travel points
    travel_points += len(current_place[1])
    # Add the current destination name to the list of valid travel destinations
    destinations.append(current_place[1])

# Print the list of valid travel destinations and the total number of travel points
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
