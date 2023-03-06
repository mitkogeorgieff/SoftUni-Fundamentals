budget = float(input())
flower_price = float(input())
eggs_price = flower_price * 0.75
milk_price = (flower_price * 1.25) * 0.25
cnt = 0
eggs_cnt = 0
loaf_price = flower_price + eggs_price + milk_price
while loaf_price <= budget:
    cnt += 1
    budget -= loaf_price
    eggs_cnt += 3

    if cnt % 3 == 0:
        eggs_cnt -= cnt - 2

print(f'You made {cnt} loaves of Easter bread! Now you have {eggs_cnt} eggs and {budget:.2f}BGN left.')