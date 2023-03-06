n = int(input())
total = 0
capacity = 255

for _ in range(n):
    liters_of_water = int(input())
    if total + liters_of_water > capacity:
        print('Insufficient capacity!')
    else:
        total += liters_of_water
print (total)