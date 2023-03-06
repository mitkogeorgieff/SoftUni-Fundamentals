def sum_numbers(first_num, second_num):
    return first_num + second_num


def subtract(sum_num, third_num):
    return sum_num - third_num


def add_and_subtract(first_num, second_num, third_num):
    sum_num = sum_numbers(first_num, second_num)
    rez = subtract(sum_num, third_num)
    return rez


a = int(input())
b = int(input())
c = int(input())

print(add_and_subtract(a, b, c))