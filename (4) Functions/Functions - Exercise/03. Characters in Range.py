a = input()
b = input()


def ascii_to_chr(first_chr, second_chr):
    list_chr = []
    for i in range(ord(first_chr)+1, ord(second_chr)):
        list_chr.append(chr(i))
    return list_chr


rez = ascii_to_chr(a, b)
print(' '.join(rez))
