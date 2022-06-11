import math
group_size = int(input())
days = int(input())
money = 0
group_count = 0
for day in range(1, days + 1):
    money += 50
    if day % 15 == 0:
        group_size += 5
    if day % 10 == 0:
        group_size -= 2
    if day % 5 == 0:
        money += group_size * 20
        if day % 3 == 0:
            money -= group_size * 2
    if day % 3 == 0:
        money -= group_size * 3
    money -= group_size * 2
money /= group_size
print(f'{group_size} companions received {math.floor(money)} coins each.')


