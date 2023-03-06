cards = input().split()
counter = int(input())

for _ in range(counter):
    f_half = []
    s_half = []

    for idx in range(1, len(cards) - 1):
        card = cards[idx]
        if idx < len(cards) / 2:
            f_half.append(card)
        else:
            s_half.append(card)

    shuffled = []
    f_idx = 0
    s_idx = 0
    for i in range(len(f_half) * 2):
        if i % 2 == 0:
            shuffled.append(s_half[s_idx])
            s_idx += 1
        else:
            shuffled.append(f_half[f_idx])
            f_idx += 1

    cards = [cards[0]] + shuffled + [cards[-1]]

print(cards)

# ace, two, three, four, five, six