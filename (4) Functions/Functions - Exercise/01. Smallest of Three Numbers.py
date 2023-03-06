a = int(input())
b = int(input())
c = int(input())

list_numbers = [a, b, c]


def smllest_num(num):
    return min(list_numbers)


min_number = smllest_num(list_numbers)
print(min_number)
