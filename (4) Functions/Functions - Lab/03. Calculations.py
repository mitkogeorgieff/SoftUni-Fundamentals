input_op = input()
f_num = int(input())
s_num = int(input())


def calc(a, b, operator):
    res = 'None'
    if operator == 'multiply':
        res = a * b
    elif operator == 'divide':
        res = a // b
    elif operator == 'add':
        res = a + b
    elif operator == 'subtract':
        res = a - b
    return res


print(calc(f_num, s_num, input_op))
