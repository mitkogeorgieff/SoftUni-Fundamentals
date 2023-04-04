password = input()

while True:
    command = input()

    # If the user enters "Complete", exit the loop
    if command == "Complete":
        break

    # Split the user command into a list of strings to extract the command and its arguments
    command_att = command.split()

    # If the command is to make a character uppercase
    if command_att[0] == "Make" and command_att[1] == "Upper":
        # Get the index of the character to uppercase and update the password accordingly
        index = int(command_att[2])
        password = password[:index] + password[index].upper() + password[index + 1:]
        # Print the updated password
        print(password)

    # If the command is to make a character lowercase
    elif command_att[0] == "Make" and command_att[1] == "Lower":
        # Get the index of the character to lowercase and update the password accordingly
        index = int(command_att[2])
        password = password[:index] + password[index].lower() + password[index + 1:]
        # Print the updated password
        print(password)

    # If the command is to insert a character at a specific index
    elif command_att[0] == "Insert":
        # Get the index and character to insert, and update the password accordingly
        index = int(command_att[1])
        char = command_att[2]
        # If the index is out of range, skip this command and continue to the next one
        if len(password) < index - 1:
            continue
        else:
            password = password[:index] + char + password[index:]
            # Print the updated password
            print(password)

    # If the command is to replace a character with another one
    elif command_att[0] == "Replace":
        # Get the character to replace, the value to add to its ASCII code, and the new character
        char = command_att[1]
        value = int(command_att[2])
        new_char = chr(ord(char) + value)
        # If the character is not in the password, skip this command and continue to the next one
        if char in password:
            password = password.replace(char, new_char)
            # Print the updated password
            print(password)
        else:
            continue

    # If the command is to validate the password
    elif command_att[0] == "Validation":
        # Check the password meets the required criteria
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        for ch in password:
            if ch.isalpha() or ch.isdigit() or ch == "_":
                continue
            else:
                print("Password must consist only of letters, digits and _!")
        if password == password.lower():
            print("Password must consist at least one uppercase letter!")
        if password == password.upper():
            print("Password must consist at least one lowercase letter!")
        if any(char.isdigit() for char in password):
            continue
        else:
            print("Password must consist at least one digit!")
