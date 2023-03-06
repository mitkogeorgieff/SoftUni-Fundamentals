numbers = input().split()
list = []

for i in numbers:
    list.append(abs(float(i)))
print(list)