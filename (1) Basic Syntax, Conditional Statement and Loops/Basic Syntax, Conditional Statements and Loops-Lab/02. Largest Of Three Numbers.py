f_num = int(input())
s_num = int(input())
t_num = int(input())

if f_num > s_num and f_num > t_num:
    print(f_num)
elif s_num > f_num and s_num > t_num:
    print(s_num)
else:
    print(t_num)