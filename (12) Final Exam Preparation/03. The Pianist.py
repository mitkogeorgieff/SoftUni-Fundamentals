# Prompt the user to enter the number of pieces in the collection
pieces = int(input())

# Create an empty dictionary to store the pieces, with each piece as a key and a dictionary of composer and key as the value
pieces_collection = {}
for num in range(pieces):
    piece, composer, key = input().split('|')
    pieces_collection[piece] = {composer: key}

while True:
    command = input()

    if command == "Stop":
        break

    current_command = command.split('|')

    # If the command is "Add", add a new piece to the collection
    if current_command[0] == 'Add':
        piece = current_command[1]
        composer = current_command[2]
        key = current_command[3]
        if piece in pieces_collection:
            # If the piece already exists in the collection, print an error message and continue to the next command
            print(f'{piece} is already in the collection!')
            continue
        pieces_collection[piece] = {composer: key}
        print(f'{piece} by {composer} in {key} added to the collection!')

    # If the command is "Remove", remove a piece from the collection
    elif current_command[0] == 'Remove':
        piece = current_command[1]
        if piece in pieces_collection:
            del pieces_collection[piece]
            print(f'Successfully removed {piece}!')
            continue
        print(f'Invalid operation! {piece} does not exist in the collection.')

    # If the command is "ChangeKey", change the key of a piece in the collection
    elif current_command[0] == 'ChangeKey':
        piece = current_command[1]
        key = current_command[2]
        if piece in pieces_collection:
            value = pieces_collection[piece]
            composer = ''
            for k in value.keys():
                composer = k
            # Update the key for the specified piece
            pieces_collection[piece][composer] = key
            print(f'Changed the key of {piece} to {key}!')
            continue
        print(f'Invalid operation! {piece} does not exist in the collection.')

# Print information about each piece in the collection
for piece, value in pieces_collection.items():
    curr_value = value.keys()
    for k in curr_value:
        composer = k
        key = pieces_collection[piece][composer]
        print(f'{piece} -> Composer: {composer}, Key: {key}')
