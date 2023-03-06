def find_idx(seq, el):
    for i in range(len(seq)):
        if seq[i] == el:
            return i
    return -1

products = input().split('!')

while True:
    line = input()
    if line == "Go Shopping!":
        break

    command_args = line.split()
    command = command_args[0]
    product = command_args[1]

    if command == 'Urgent':
        if product not in products:
            products.insert(0, product)
    elif command == "Unnecessary":
        if product in products:
            products.remove(product)
    elif command == 'Correct':
        new_product = command_args[2]
        if product in products:
            idx = find_idx(products, product)
            if idx == -1:
                continue
            products[idx] = new_product
    elif command == "Rearrange":
        if product in products:
            products.remove(product)
            products.append(product)

print(", ".join(products))
