quantity = int(input())
r_days = int(input())

ornamentSet = 2
treeSkirt = 5
treeGarland = 3
treeLights = 15

budget = 0
total_spirit = 0

for curr_day in range (1, r_days + 1):
    if curr_day % 11 == 0:
        quantity += 2
    if curr_day % 2 == 0:
        budget += ornamentSet * quantity
        total_spirit += 5
    if curr_day % 3 == 0:
        budget += (treeSkirt + treeGarland) * quantity
        total_spirit += 13
    if curr_day % 5 == 0:
        budget += treeLights * quantity
        total_spirit += 17
        if curr_day % 3 == 0:
            total_spirit += 30
    if curr_day % 10 == 0:
        budget += treeSkirt + treeGarland + treeLights
        total_spirit -= 20
if r_days % 10 == 0:
    total_spirit -= 30

print(f'Total cost: {budget}')
print(f'Total spirit: {total_spirit}')
