from math import ceil
numbers = [int(x) for x in input().split(',')]
groups_cnt = ceil((max(numbers) / 10))

start = 1
end = 10

for idx in range(1, groups_cnt + 1):
    group_list = [x for x in numbers if start <= x <= end]
    print(f"Group of {idx}0's: {group_list}")

    start += 10
    end += 10


# numbers = list(map(int, input().split(', ')))
# for group in range(1, 11):
#     if len(numbers) == 0:
#         break
#     group_list = [num for num in numbers if num <= (group * 10)]
#     numbers = [num for num in numbers if num not in group_list]
#     print(f"Group of {group}0's: {group_list}")