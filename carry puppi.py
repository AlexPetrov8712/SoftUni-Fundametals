food = int(input()) * 1000
command = input()
while command != 'Adopted':
    foods = int(command)
    food -= foods
    command = input()
if food >= 0:
    print(f'Food is enough! Leftovers: {food} grams.')
else:
    print(f'Food is not enough. You need {abs(food)} grams more.')