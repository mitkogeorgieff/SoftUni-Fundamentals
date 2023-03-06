coffee_counter = 0

while True:
    line = input()
    if line == 'END':
        break

    if line == 'coding' or line == 'movie' or line == 'dog' or line == 'cat':
        coffee_counter += 1
    if line == 'CODING' or line == 'MOVIE' or line == 'DOG' or line == 'CAT':
        coffee_counter += 2

if coffee_counter > 5:
    print('You need extra sleep')
else:
    print(coffee_counter)