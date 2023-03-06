n = int(input())
search_condition = input()
output = []
output_with_word = []

for _ in range(n):
    current_string = input()
    output.append(current_string)

    if search_condition in current_string:
        output_with_word.append(current_string)

print(output)
print(output_with_word)