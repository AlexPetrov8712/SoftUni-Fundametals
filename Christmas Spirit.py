quantity = int(input())
days = int(input())

total_spirit = 0
budget = 0

for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 15 == 0:
        total_spirit += 30
    if i % 2 == 0:
        total_spirit += 5
        budget += quantity * 2
    if i % 3 == 0:
        total_spirit += 13
        budget += quantity * 8
    if i % 5 == 0:
        total_spirit += 17
        budget += quantity * 15
    if i % 10 == 0:
        total_spirit -= 20
        budget += 23
if days % 10 == 0:
    total_spirit -= 30

print(f'Total cost: {budget}\nTotal spirit: {total_spirit}')