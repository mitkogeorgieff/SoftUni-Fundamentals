def emoticon_finder(string):
    for index, char in enumerate(string):
        if char == ':':
            print(f'{char}{string[index + 1]}')


text = input()
emoticon_finder(text)
