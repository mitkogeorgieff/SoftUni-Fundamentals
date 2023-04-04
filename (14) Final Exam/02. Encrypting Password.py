import re

num = int(input())

# Define a regular expression pattern to match valid passwords in a line
pattern = r"(.+)>(?P<password>\d{3}\|[a-z]{3}\|[A-Z]{3}\|[^<>]{3})<\1"

# Iterate over the input lines
for i in range(num):
    line = input()

    # Find all matches of the password pattern in the line
    valid_passwords = re.finditer(pattern, line)

    # Collect all valid passwords in a list
    final = []
    for valid in valid_passwords:
        final.append(valid.group('password'))

    # If at least one valid password was found, format and print it
    if final:
        second = ""
        for some in final:
            # Remove the '|' characters from the password
            second = some.replace("|", "")
        print(f"Password: {second}")
    else:
        print(f"Try another password!")
