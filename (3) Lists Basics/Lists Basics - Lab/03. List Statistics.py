n = int(input())
list_positive = []
list_negative = []

for i in range(n):
    current_value = int(input())

    if current_value >= 0:
        list_positive.append(current_value)
    else:
        list_negative.append(current_value)

print(list_positive)
print(list_negative)
print(f'Count of positives: {len(list_positive)}')
print(f'Sum of negatives: {sum(list_negative)}')