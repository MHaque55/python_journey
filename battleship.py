row_num = 0
col_num = 0
board = [[None] * 10] * 10
for i in range(0, 10):
    for j in range(0, 10):
        board[i][j] = " -, - "

for i in range(0, 10):
    print("    " + str(i) + "   ", end='')

print()

for i in board:
    print(row_num, end='')
    row_num = row_num + 1
    for j in i:
        print("|" + j, end='|')
    print()
