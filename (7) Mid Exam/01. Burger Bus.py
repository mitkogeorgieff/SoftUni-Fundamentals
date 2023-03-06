cities_visited = int(input())
cities_cnt = 0
tot_profit = 0

while True:
    if cities_visited <= 0 or cities_visited > 15:
        break
    cities_cnt += 1
    city_name = input()
    income = float(input())
    expenses = float(input())

    if cities_cnt % 5 == 0 and income > 0:
        if "rainy" not in city_name.lower():
            income = income * 0.9

    if cities_cnt % 3 == 0 and expenses > 0:
        expenses = expenses * 1.5

    profit = income - expenses
    tot_profit += profit

    print(f"In {city_name} Burger Bus earned {profit:.2f} leva.")

    if cities_cnt == cities_visited:
        break

print(f"Burger Bus total profit: {tot_profit:.2f} leva.")
