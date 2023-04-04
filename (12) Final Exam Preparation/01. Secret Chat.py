message = input()
command = input()

while command != "Reveal":
    error = False

    # Split the command into a list of words
    current_command = command.split(':|:')

    # Get the instruction, index, substring, and replacement (if it exists) from the command
    instruction = current_command[0]
    index = current_command[1]
    substring = current_command[1]

    try:
        replacement = current_command[2]
    except IndexError:
        # If there is no replacement, set it to None
        replacement = None

    # If the instruction is "InsertSpace"
    if instruction == "InsertSpace":
        # Get the index specified in the command
        index = int(index)
        # Insert a space at the specified index in the message
        message = message[:index] + ' ' + message[index:]

    # If the instruction is "Reverse"
    elif instruction == "Reverse":
        # Check if the substring exists in the message
        if substring in message:
            # Get the index of the substring
            index = message.index(substring)
            # Remove the substring from the message
            how_long = len(substring)
            for msg in range(how_long):
                message = message[:index] + message[index + 1:]
            # Add the reversed substring to the end of the message
            message += substring[::-1]
        else:
            # If the substring is not found, set error to True and print an error message
            error = True
            print("error")

    # If the instruction is "ChangeAll"
    elif instruction == "ChangeAll":
        # Replace all occurrences of the substring with the replacement in the message
        message = message.replace(substring, replacement)

    # If there is no error, print the updated message
    if not error:
        print(message)

    # Ask the user for another command
    command = input()

# When the user enters "Reveal", print the final message
print(f"You have a new text message: {message}")
