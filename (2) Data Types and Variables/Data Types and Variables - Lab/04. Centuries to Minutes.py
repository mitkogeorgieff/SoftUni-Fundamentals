centuries = int(input())
years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
min = hours * 60

print(
    f'{centuries} centuries = '
    f'{years} years = '
    f'{days} days = '
    f'{hours} hours = '
    f'{min} minutes'
)
