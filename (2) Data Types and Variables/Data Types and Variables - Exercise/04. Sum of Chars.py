n = int(input())
result = 0
for _ in range(n):
    symbol = input()
    result += ord(symbol)

print(f'The sum equals: {result}')