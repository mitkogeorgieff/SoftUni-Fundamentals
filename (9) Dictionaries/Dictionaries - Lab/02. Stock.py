elements = input().split(' ')
stock = {}

for i in range(0, len(elements), 2):
    stock[elements[i]] = int(elements[i + 1])

search_products = input().split(' ')

for curr_product in search_products:
    if curr_product in stock:
        print(f"We have {stock[curr_product]} of {curr_product} left")
    else:
        print(f"Sorry, we don't have {curr_product}")

