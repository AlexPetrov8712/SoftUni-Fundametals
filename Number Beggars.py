string_list = input().split(', ')
count_beggars = int(input())
final_list = []
counter_index = 0
sum_list_digits = []
for element in string_list:
    sum_list_digits.append(int(element))
while counter_index < count_beggars:
    sum_beggars = 0
    for current_index in range(counter_index, len(sum_list_digits), count_beggars):
        sum_beggars += sum_list_digits[current_index]
    counter_index += 1
    final_list.append(sum_beggars)
print(final_list)