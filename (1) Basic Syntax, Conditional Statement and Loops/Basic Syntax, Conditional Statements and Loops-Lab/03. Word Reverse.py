word = input()
r_word = ''

for i in range(len(word) - 1, -1, -1):
    r_word += word[i]
print(r_word)

# hack print(word[::-1])