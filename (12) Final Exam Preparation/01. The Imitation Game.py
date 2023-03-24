encrypted_message = input()

while True:
    input_command = input()

    # If the user enters "Decode", break out of the loop
    if input_command == "Decode":
        break

    # Split the input command into parts based on the "|" character
    split_data = input_command.split("|")

    # If the command is "Move", shift the letters in the message by a certain number
    if split_data[0] == "Move":
        number_of_letters = int(split_data[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]

    # If the command is "Insert", insert a certain value at a certain index in the message
    elif split_data[0] == "Insert":
        index = int(split_data[1])
        value = split_data[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    # If the command is "ChangeAll", replace all occurrences of a certain substring with a replacement string
    elif split_data[0] == "ChangeAll":
        substring = split_data[1]
        replacement = split_data[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

print(f"The decrypted message is: {encrypted_message}")
