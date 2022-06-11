n = int(input())
capacity = 255
total = 0
for i in range(n):
    litters = int(input())
    if litters > capacity:
        print('Insufficient capacity!')
        continue
    capacity -= litters
    total += litters
print(total)
