words = input().split(" ")
characters_dictionary = {}

for word in words:
    for letter in word:
        if letter in characters_dictionary:
            characters_dictionary[letter] += 1
        elif letter not in characters_dictionary:
            characters_dictionary[letter] = 1

for letter, count in characters_dictionary.items():
    print(f"{letter} -> {count}")
