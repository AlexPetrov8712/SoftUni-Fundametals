factor = int(input())
count = int(input())
lists = []
for number in range(1, count + 1):
    number *= factor
    lists.append(number)
print(lists)
