num = int(input())
for i in range(num):
    text = input()
    if ',' in text or '_' in text or '.' in text:
        print(f'{text} is not pure!')
    else:
        print(f'{text} is pure.')
