def substring(first_string, string):
    second_string = string
    while first_string in second_string:
        second_string = second_string.replace(first_string, '')

    return second_string


first = input()
second = input()
print(substring(first, second))
