raw_activation_key = input()
command = input()

while command != "Generate":
    # Split the command into a list of words
    operation = command.split(">>>")

    # If the first word is "Contains"
    if operation[0] == "Contains":
        # Get the substring specified in the command
        substring = operation[1]
        # Check if the substring exists in the raw activation key
        if substring in raw_activation_key:
            # If the substring is found, print a message
            print(f"{raw_activation_key} contains {substring}")
        else:
            # If the substring is not found, print a message
            print("Substring not found!")

    # If the first word is "Flip"
    elif operation[0] == "Flip":
        # Get the case ("Upper" or "Lower") and indices specified in the command
        upper_lower = operation[1]
        start_index = int(operation[2])
        end_index = int(operation[3])
        # Modify the specified substring based on the case parameter
        if upper_lower == "Upper":
            raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].upper() + raw_activation_key[end_index:]
        elif upper_lower == "Lower":
            raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].lower() + raw_activation_key[end_index:]
        # Print the updated raw activation key
        print(raw_activation_key)

    # If the first word is "Slice"
    elif operation[0] == "Slice":
        # Get the indices specified in the command
        start_index = int(operation[1])
        end_index = int(operation[2])
        # Remove the specified substring from the raw activation key
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        # Print the updated raw activation key
        print(raw_activation_key)

    # Ask the user for another command
    command = input()

# When the user enters "Generate", print the final activation key
print(f"Your activation key is: {raw_activation_key}")
