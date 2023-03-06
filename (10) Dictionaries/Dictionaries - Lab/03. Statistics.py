products_inv = {}

while True:
    command = input()
    if command == "statistics":
        break

    command = command.split(": ")
    product = command[0]
    quantity = int(command[1])

    if product not in products_inv:
        products_inv[product] = quantity
    else:
        products_inv[product] += quantity

print(f"Products in stock:")
prod_repr = [f' - {item}: {str(products_inv[item])}' for item in products_inv]
print('\n'.join(prod_repr))
print(f"Total Products: {len(products_inv)}")
print(f"Total Quantity: {sum(products_inv.values())}")
