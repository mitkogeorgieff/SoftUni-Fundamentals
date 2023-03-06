n = int(input())

for num in range(1, n+1):
    is_special = False
    num_as_str = str(num)
    sum_digits = 0

    for ch in num_as_str:
        sum_digits += int(ch)

    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        is_special = True

    print(f'{num} -> {is_special}')