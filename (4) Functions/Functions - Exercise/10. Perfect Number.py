def is_perfect(num):
    sum = 0
    for divisors in range(1, number):
        if number % divisors == 0:
            sum += divisors
    if num == sum:
        return 'We have a perfect number!'
    return "It's not so perfect."



number = int(input())

print(is_perfect(number))