num = int(input())
sums = 0

for i in range(num):
    text = input()
    sums += ord(text)
print(f'The sum equals: {sums}')


