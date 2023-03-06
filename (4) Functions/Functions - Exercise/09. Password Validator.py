def is_valid_len(passwd):
    return 6 <= len(passwd) <= 10


def is_alnum(passwd):
    return passwd.isalnum()


def has_two_digits(passwd):
    digit_cnt = 0
    for ch in passwd:
        if ch.isdigit():
            digit_cnt += 1
    return digit_cnt >= 2


in_pass = input()
is_valid = True

if not is_valid_len(in_pass):
    is_valid = False
    print('Password must be between 6 and 10 characters')
if not is_alnum(in_pass):
    is_valid = False
    print('Password must consist only of letters and digits')
if not has_two_digits(in_pass):
    is_valid = False
    print('Password must have at least 2 digits')

if is_valid:
    print('Password is valid')
