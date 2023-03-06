divisor = int(input())
boundary = int(input())
largest_n = 0

for num in range(1, boundary + 1):
    if num % divisor == 0:
        largest_n = num
print(largest_n)
