while True:
    line = input()
    if line == 'Welcome!':
        print('Welcome to Hogwarts.')
        break

    if len(line) < 5:
        print(f'{line} goes to Gryffindor.')
    if len(line) == 5:
        print(f'{line} goes to Slytherin.')
    if len(line) == 6:
        print(f'{line} goes to Ravenclaw.')
    if len(line) > 6 and line != 'Voldemort':
        print(f'{line} goes to Hufflepuff.')

    if line == 'Voldemort':
        print('You must not speak of that name!')
        break
