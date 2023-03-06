todo_list = [0] * 10

while True:
    command = input()

    if command == "End":
        break

    importance, task = command.split('-')
    importance = int(importance)
    idx = importance - 1
    todo_list[idx] = task

print([task for task in todo_list if task != 0])
