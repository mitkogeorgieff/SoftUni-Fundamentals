import re

string = input()
pattern = r"([|#])(\w+(\s\w+|\S))\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"

# Use the regular expression pattern to find all food items in the input string
food = re.findall(pattern, string)

# Calculate the total number of calories in all food items
needed_calories_per_day = 2000
total_calories = 0
for element in food:
    total_calories += int(element[-1])

# Calculate how many days the food will last based on the total number of calories
days_to_last = total_calories // needed_calories_per_day
print(f"You have food to last you for: {days_to_last} days!")

# Print information about each food item
for elements in food:
    item = elements[1]  # Get the name of the food item from the second capturing group
    date = elements[3]  # Get the best before date from the fourth capturing group
    calories = elements[4]  # Get the number of calories from the fifth capturing group
    print(f"Item: {item}, Best before: {date}, Nutrition: {calories}")
