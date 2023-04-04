password = input()
command = input()

while command != "Done":
    # Split the command into a list of words
    activity = command.split(' ')

    # If the first word is "TakeOdd"
    if activity[0] == "TakeOdd":
        # Use list comprehension to create a new list with every other character in the password
        string = [char for index, char in enumerate(password) if index % 2 != 0]
        # Join the list back into a string to update the password
        password = ''.join(string)
        # Print the updated password
        print(password)

    # If the first word is "Cut"
    elif activity[0] == "Cut":
        # Get the index and length specified in the command
        index = int(activity[1])
        length = int(activity[2])
        # Use string slicing to remove the specified substring from the password
        password = password[:index] + password[index + length:]
        # Print the updated password
        print(password)

    # If the first word is "Substitute"
    elif activity[0] == "Substitute":
        # Get the substring and substitute specified in the command
        substring = activity[1]
        substitute = activity[2]
        # Check if the substring exists in the password
        if substring in password:
            # Use the replace() method to substitute the substring with the specified substitute
            password = password.replace(substring, substitute)
            # Print the updated password
            print(password)
        else:
            # If the substring is not found, print a message
            print("Nothing to replace!")

    # Ask the user for another command
    command = input()

# When the user enters "Done", print the final password
print(f"Your password is: {password}")