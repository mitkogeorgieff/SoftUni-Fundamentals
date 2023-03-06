array_integers = list(map(int, input().split(' ')))


while True:
    command = input()
    if command == 'end':
        break

    if command == 'decrease':
        for element in range(len(array_integers)):
            array_integers[element] -= 1
        continue
    list_command = command.split(' ')
    index1 = int(list_command[1])
    index2 = int(list_command[2])
    if list_command[0] == 'swap':
        array_integers[index1], array_integers[index2] = array_integers[index2], array_integers[index1]
    if list_command[0] == 'multiply':
        array_integers[index1] *= array_integers[index2]

print(*array_integers, sep=', ')