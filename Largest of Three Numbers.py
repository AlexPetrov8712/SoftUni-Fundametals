num_one = int(input())
num_two = int(input())
num_third = int(input())

if num_one > num_two and num_one > num_third:
    print(num_one)
elif num_two > num_one and num_two > num_third:
    print(num_two)
else:
    print(num_third)