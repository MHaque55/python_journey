num_ships = 4
placement = ["left", "right", "up", "down"]
board = [[None] * 10] * 10
for i in range(0, 10):
    for j in range(0, 10):
        board[i][j] = " -, - "


def display(map):
    row_num = 0
    for i in range(0, 10):
        print("    " + str(i) + "   ", end='')
    print()
    for i in map:
        print(row_num, end='')
        row_num = row_num + 1
        for j in i:
            print("|" + j, end='|')
        print()


#def ai_turn(map):

display(board)