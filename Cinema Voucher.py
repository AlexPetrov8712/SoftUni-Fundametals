voucher = int(input())
command = input()
ticket = 0
other = 0
price = 0
while command != 'End':
    if len(command) > 8:
        price = ord(command[0]) + ord(command[1])
        if price > voucher:
            break
        voucher -= price
        ticket += 1
    elif len(command) <= 8:
        price = ord(command[0])
        if price > voucher:
            break
        voucher -= price
        other += 1
    command = input()
print(f'{ticket}')
print(f'{other}')
