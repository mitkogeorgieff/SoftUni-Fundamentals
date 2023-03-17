import re
string = input().lower()
word = input().lower()

matches = re.findall(f'\\b({word})\\b', string)
print(len(matches))
