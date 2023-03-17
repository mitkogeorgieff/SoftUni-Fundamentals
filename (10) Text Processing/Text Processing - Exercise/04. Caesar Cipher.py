def ecode_text(string):
    result = ''
    for char in string:
        result += chr(ord(char) + 3)
    return result


text = input()
print(ecode_text(text))
