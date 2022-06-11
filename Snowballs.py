num = int(input())
max_value = 0
output = ''

for i in range(num):
    snow = int(input())
    time = int(input())
    quality = int(input())
    value = int(snow / time) ** quality
    if value > max_value:
        max_value = value
        output = f'{snow} : {time} = {value} ({quality})'

print(output)

