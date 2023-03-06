while True:
    line = input()
    if line == 'End':
        break

    if line == 'SoftUni':
        continue

    new_line = ''
    for ch in line:
        new_line += 2 * ch
    print(new_line)