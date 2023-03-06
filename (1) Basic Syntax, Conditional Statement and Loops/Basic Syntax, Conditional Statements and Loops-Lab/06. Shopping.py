budget = int(input())
price = input()

while price != 'End':
    curent_price = int(price)

    budget -= curent_price

    if budget < 0:
        print('You went in overdraft!')
        break
    price = input()

else:
    print('You bought everything needed.')