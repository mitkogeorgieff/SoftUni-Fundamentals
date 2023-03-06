orders = int(input())
tot = 0
for _ in range(orders):
    price = float(input())
    days = int(input())
    capsules = int(input())

    if price < 0.01 or price > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules < 1 or capsules > 2000:
        continue
    order_total = price * days * capsules
    tot += order_total

    print(f'The price for the coffee is: ${order_total:.2f}')


print(f'Total: ${tot:.2f}')
