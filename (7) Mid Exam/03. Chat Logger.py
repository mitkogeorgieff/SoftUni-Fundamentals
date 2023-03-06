def find_chat_log(input_list, element_to_edit):
    for i in range(len(input_list)):
        if input_list[i] == element_to_edit:
            return i
    return -1

chat_log = []

while True:
    msg_input = input()
    if msg_input == 'end':
        break

    list_command = msg_input.split(' ')
    if list_command[0] == 'Chat':
        chat_log.append(list_command[1])
    elif list_command[0] == 'Delete':
        if list_command[1] in chat_log:
            chat_log.remove(list_command[1])
    elif list_command[0] == 'Edit':
        old_msg = list_command[1]
        corrected_msg = list_command[2]
        idx = find_chat_log(chat_log, old_msg)
        if idx == -1:
            continue
        chat_log[idx] = corrected_msg
    elif list_command[0] == 'Pin':
        if list_command[1] in chat_log:
            chat_log.remove(list_command[1])
            chat_log.append(list_command[1])
    elif list_command[0] == 'Spam':
        for i in range(1, len(list_command)):
            chat_log.append(list_command[i])

print(*chat_log, sep='\n')
