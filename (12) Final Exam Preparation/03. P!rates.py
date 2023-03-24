data = input()
cities = {}

# Loop through each city and add its population and gold to the cities dictionary
while data != "Sail":
    # Split the input data into city name, population, and gold values
    split_data = data.split("||")
    city = split_data[0]
    population = int(split_data[1])
    gold = int(split_data[2])

    # If the city is not already in the dictionary, add it
    if city not in cities:
        cities[city] = {"population": population, "gold": gold}
    # If the city is already in the dictionary, update its population and gold values
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold

    # Get the next city data from the user
    data = input()

data = input()
while data != "End":
    # Split the input data into command and city values
    split_data = data.split("=>")
    command = split_data[0]
    city = split_data[1]

    # If the command is "Plunder", reduce the city's population and gold and print a message
    if command == "Plunder":
        people = int(split_data[2])
        gold = int(split_data[3])

        cities[city]["population"] -= people
        cities[city]["gold"] -= gold

        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")

        # If the city's population or gold drops to 0 or below, remove it from the cities dictionary and print a message
        if cities[city]["population"] <= 0 or cities[city]["gold"] <= 0:
            del cities[city]
            print(f"{city} has been wiped off the map!")

    # If the command is "Prosper", add gold to the city's gold value (if it's not negative) and print a message
    elif command == "Prosper":
        gold = int(split_data[2])
        if gold >= 0:
            cities[city]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")
        else:
            print("Gold added cannot be a negative number!")

    # Get the next command from the user
    data = input()

if not cities:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, values in cities.items():
        print(f"{city} -> Population: {cities[city]['population']} citizens, Gold: {cities[city]['gold']} kg")
