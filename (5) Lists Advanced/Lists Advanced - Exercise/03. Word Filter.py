words = input().split(' ')
words_list = [word for word in words if len(word) % 2 == 0]
print('\n'.join(words_list))
