input_operator = input()
one_num = int(input())
two_num = int(input())


def solve(a, b, operator):
    result = None
    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = a // b
    elif operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b
    return result


print(solve(one_num, two_num, input_operator))
