row_1 = input().split()
row_2 = input().split()
row_3 = input().split()

is_winner = False
winner = ""

if row_1[0] == row_1[1] == row_1[2] != "0":
    is_winner = True
    winner = row_1[0]
elif row_2[0] == row_2[1] == row_2[2] != "0":
    is_winner = True
    winner = row_2[0]
elif row_3[0] == row_3[1] == row_3[2] != "0":
    is_winner = True
    winner = row_3[0]

if row_1[0] == row_2[0] == row_3[0] != "0":
    is_winner = True
    winner = row_1[0]
elif row_1[1] == row_2[1] == row_3[1] != "0":
    is_winner = True
    winner = row_1[1]
elif row_1[2] == row_2[2] == row_3[2] != "0":
    is_winner = True
    winner = row_1[2]

if row_1[0] == row_2[1] == row_3[2] != "0":
    is_winner = True
    winner = row_1[0]
elif row_1[2] == row_2[1] == row_3[0] != "0":
    is_winner = True
    winner = row_1[2]

if not is_winner:
    print("Draw!")
else:
    if winner == "1":
        print("First player won")
    elif winner == "2":
        print("Second player won")
