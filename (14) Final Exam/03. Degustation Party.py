# Initialize a dictionary to store the guests and their liked meals
degustation_party_guests = {}

# Initialize a counter for unliked meals
unliked_cnt = 0

while True:
    command = input()
    if command == "Stop":
        break

    # Split the command into its action, guest, and meal components
    action, guest, meal = command.split("-")

    # If the action is "Like", add the meal to the guest's collection
    if action == "Like":
        if guest not in degustation_party_guests:
            degustation_party_guests[guest] = []

        if meal not in degustation_party_guests[guest]:
            degustation_party_guests[guest].append(meal)

    # If the action is "Dislike", remove the meal from the guest's collection and increment the unliked counter
    elif action == "Dislike":
        if guest not in degustation_party_guests:
            print(f"{guest} is not at the party.")
        elif meal not in degustation_party_guests[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            degustation_party_guests[guest].remove(meal)
            unliked_cnt += 1
            print(f"{guest} doesn't like the {meal}.")

# Print the final collection of liked meals for each guest
for guest, meals in degustation_party_guests.items():
    print(f"{guest}: {', '.join(meals)}")

# Print the total number of unliked meals
print(f"Unliked meals: {unliked_cnt}")
