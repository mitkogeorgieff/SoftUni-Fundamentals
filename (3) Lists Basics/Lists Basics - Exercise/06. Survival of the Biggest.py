numbers = [int(x) for x in input().split()]
numbers_to_remove = int(input())

for _ in range(numbers_to_remove):
    min_number = min(numbers)
    numbers.remove(min_number)

print(', '.join([str(x) for x in numbers]))