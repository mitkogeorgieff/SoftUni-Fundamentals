def return_min(min_num):
    return min(min_num)


def return_max(max_num):
    return max(max_num)


def return_sum(sum_num):
    return sum(sum_num)


list_num = [int(x) for x in input().split()]

print(f'The minimum number is {return_min(list_num)}')
print(f'The maximum number is {return_max(list_num)}')
print(f'The sum number is: {return_sum(list_num)}')