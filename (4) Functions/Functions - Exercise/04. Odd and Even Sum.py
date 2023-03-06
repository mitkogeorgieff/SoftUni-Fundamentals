def odd_even_sum(number):
    even_sum = 0
    odd_sum = 0

    for digit in number:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return odd_sum, even_sum


numbers_as_str = input()
sum_of_odd_digits, sum_of_even_digits = odd_even_sum(numbers_as_str)

print(f'Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}')
