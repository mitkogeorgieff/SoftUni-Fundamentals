coffee_list = input().split()
cmd_cnt = int(input())

for i in range(cmd_cnt):
    command = input().split()

    if command[0] == 'Include':
        coffee_list.append(command[1])
    elif command[0] == 'Remove':
        if command[1] == 'first':
            num_coffees = int(command[2])
            coffee_list = coffee_list[num_coffees:]
        else:  # command[1] == 'last'
            num_coffees = int(command[2])
            coffee_list = coffee_list[:-num_coffees] if num_coffees < len(coffee_list) else []
    elif command[0] == 'Prefer':
        index1, index2 = map(int, command[1:])
        if 0 <= index1 < len(coffee_list) and 0 <= index2 < len(coffee_list):
            coffee_list[index1], coffee_list[index2] = coffee_list[index2], coffee_list[index1]
    elif command[0] == 'Reverse':
        coffee_list = coffee_list[::-1]

print(f'Coffees:\n{" ".join(coffee_list)}')