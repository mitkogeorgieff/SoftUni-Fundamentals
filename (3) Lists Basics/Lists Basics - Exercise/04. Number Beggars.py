string = input().split(', ')
cnt = int(input())

beggars = [0] * cnt

for idx in range(len(string)):
    beggar_idx = idx % cnt
    num = int(string[idx])

    beggars[beggar_idx] += num
print(beggars)