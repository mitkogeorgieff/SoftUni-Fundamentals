path = input()

path_file_arg = path.split('\\')
file_name = path_file_arg[-1]
file_name_args = file_name.split('.')

print("File name:", file_name_args[0])
print("File extension:", file_name_args[-1])
