first_row = input().split(", ")
second_row = input().split(", ")
new_line = []

for first_row_word in first_row:
    for second_row_word in second_row:
        if first_row_word in second_row_word:
            new_line.append(first_row_word)
            break
print(new_line)
