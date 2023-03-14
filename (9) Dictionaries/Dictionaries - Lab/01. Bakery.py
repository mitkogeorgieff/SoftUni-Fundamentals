bakery = input().split(' ')
dict_bakery_stock = {}

for i in range(0, len(bakery), 2):
    dict_bakery_stock[bakery[i]] = int(bakery[i + 1])

print(dict_bakery_stock)
