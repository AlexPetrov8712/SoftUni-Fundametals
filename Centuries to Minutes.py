centuries = int(input())
year = centuries * 100
days = int(year * 365.2422)
hour = int(days) * 24
minutes = int(hour) * 60
print(f'{centuries} centuries = {int(year)} years = {days} days = {hour} hours = {minutes} minutes')
