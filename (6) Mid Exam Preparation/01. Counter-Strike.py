energy = int(input())
command = input()
wins = 0

while command != 'End of battle':
    dist = int(command)
    if energy >= dist:
        energy -= dist
        wins += 1
        if wins % 3 == 0:
            energy += wins
    else:
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        break
    command = input()
else:
    print(f"wins battles: {wins}. Energy left: {energy}")