def is_palindrome(numbers: list):

    for nbr in numbers:

        if nbr == nbr[::-1]:
            print(True)
            continue
        print(False)


list_nbr = input().split(', ')
is_palindrome(list_nbr)
