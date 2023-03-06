def is_even(number):
    return number % 2 == 0


list_num = [int(x) for x in input().split()]

print(list(filter(is_even, list_num)))

