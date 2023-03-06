string = input()
n = int(input())

repeat_string = lambda inp_str, rep: inp_str * rep

print(repeat_string(string, n))
