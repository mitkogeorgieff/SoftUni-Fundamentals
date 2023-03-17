def reverse_string(string: str):
    reversed_string = string[::-1]
    return f'{string} = {reversed_string}'


word = input()
while word != "end":
    print(reverse_string(word))
    word = input()
