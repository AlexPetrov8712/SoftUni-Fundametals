n = int(input())
numbers = []
filtered = []

for i in range(n):
    current_num = int(input())
    numbers.append(current_num)
command = input()
if command == 'even':
    for current_num in numbers:
        if current_num % 2 == 0:
            filtered.append(current_num)
elif command == 'odd':
    for current_num in numbers:
        if current_num % 2 != 0:
            filtered.append(current_num)
elif command == 'negative':
    for current_num in numbers:
        if current_num < 0:
            filtered.append(current_num)
elif command == 'positive':
    for current_num in numbers:
        if current_num >= 0:
            filtered.append(current_num)
print(filtered)
