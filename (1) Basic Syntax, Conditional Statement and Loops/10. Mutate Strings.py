first = input()
second = input()

result = ''

for i in range(len(first)):
    if first[i] == second[i]:
        continue
    result = second[0:i + 1] + first[i + 1:]
    print(result)
