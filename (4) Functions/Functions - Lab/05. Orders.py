product = input()
quantity = int(input())


def calc_price(pr, qty):
    if product == 'coffee':
        return quantity * 1.50
    if product == 'water':
        return quantity * 1.00
    if product == 'coke':
        return quantity * 1.40
    if product == 'snacks':
        return quantity * 2.00


print(f'{calc_price(product, quantity):.2f}')
