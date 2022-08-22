mat = [['0:0', '0:1', '0:2'],
       ['1:0', '1:1', '1:2'],
       ['2:0', '2:1', '2:2']]

p1 = input('Player1, enter your name: ')
p2 = input('Player2, enter your name: ')

print(p1 + ' is \'O\'' + ' and ' + p2 + ' is \'X\'')
print('Nope you don\'t have any choice')


def display(dis_mat):
    for i in dis_mat:
        for j in i:
            print(j, end='     ')
        print()


def result(mat, p1, p2):
    # Horizontal
    if mat[0][0] == mat[1][0] and mat[1][0] == mat[2][0]:
        if mat[0][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    elif mat[0][1] == mat[1][1] and mat[1][1] == mat[2][1]:
        if mat[0][1] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    elif mat[2][0] == mat[2][1] and mat[2][1] == mat[2][2]:
        if mat[2][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    # Vertical
    elif mat[0][0] == mat[0][1] and mat[0][1] == mat[0][2]:
        if mat[0][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    elif mat[1][0] == mat[1][1] and mat[1][1] == mat[1][2]:
        if mat[1][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    elif mat[2][0] == mat[2][1] and mat[2][1] == mat[2][2]:
        if mat[2][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    # Diagonal
    elif mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2]:
        if mat[0][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    elif mat[0][2] == mat[1][1] and mat[1][1] == mat[2][0]:
        if mat[0][2] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    else:
        for i in mat:
            for j in i:
                if j == 'X' or j == 'O':
                    continue
                else:
                    return False
    print('Draw oh oh')
    return True


def is_valid(mat, row, col):
    if (row < 0 or row > 2) or (col < 0 or col > 2):
        print('Invalid argument, try again')
        return False
    else:
        if mat[row][col] == 'X' or mat[row][col] == 'O':
            print('Invalid argument, place already chosen, try again')
            return False
        return True


def game(mat, p1, p2):
    print('See the mat below')
    display(mat)
    print('row : column')
    while not result(mat, p1, p2):
        print(p1 + ', your turn.')
        in_row = input('Enter your row (left one) number: ')
        in_col = input('Enter your column (right one) number: ')
        row = int(in_row)
        col = int(in_col)
        while not is_valid(mat, row, col):
            in_row = input('Enter your row (left one) number: ')
            in_col = input('Enter your column (right one) number: ')
            row = int(in_row)
            col = int(in_col)
        mat[row][col] = 'O'
        display(mat)
        print(p2 + ', your turn.')
        in_row = input('Enter your row (left one) number: ')
        in_col = input('Enter your column (right one) number: ')
        row = int(in_row)
        col = int(in_col)
        while not is_valid(mat, row, col):
            in_row = input('Enter your row (left one) number: ')
            in_col = input('Enter your column (right one) number: ')
            row = int(in_row)
            col = int(in_col)
        mat[row][col] = 'X'
        display(mat)
    return True


game(mat, p1, p2)
