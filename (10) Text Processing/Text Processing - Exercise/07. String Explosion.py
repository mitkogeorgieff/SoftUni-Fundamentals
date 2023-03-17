text = input().split(">")
previous = 0
result = [text[0]]

for part in text[1:]:
    power = int(part[0])
    previous += power

    formatted_path = part[previous:]
    previous = max(previous - len(part), 0)
    result.append(formatted_path)

print('>'.join(result))
