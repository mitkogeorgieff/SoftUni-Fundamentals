n = int(input())
positive_nums = []
negative_nums = []
even_nums = []
odd_nums = []

for _ in range(n):
    current_number = int(input())

    if current_number >= 0:
        positive_nums.append(current_number)
    else:
        negative_nums.append(current_number)
    if current_number % 2 == 0:
        even_nums.append(current_number)
    else:
        odd_nums.append(current_number)

command = input()
if command == 'even':
    print(even_nums)
elif command == 'odd':
    print(odd_nums)
elif command == 'positive':
    print(positive_nums)
else:
    print(negative_nums)