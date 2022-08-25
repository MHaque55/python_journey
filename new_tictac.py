mat = [['00', '|', '02', '|', '04'],
       ['-', '+', '-', '+', '-'],
       ['20', '|', '22', '|', '24'],
       ['-', '+', '-', '+', '-'],
       ['40', '|', '42', '|', '44']]
for i in mat:
    for j in i:
        print(j, end='')
    print()

p1 = input('Player1, enter your name: ')
p2 = input('Player2, enter your name: ')

print(p1 + ' is \'O\'' + ' and ' + p2 + ' is \'X\'')
print('Nope you don\'t have any choice')


def display(dis_mat):
    for i in dis_mat:
        for j in i:
            print(j, end=' ')
        print()


def result(mat, p1, p2):
    # Verical
    if mat[0][0] == mat[2][0] and mat[2][0] == mat[4][0]:
        if mat[0][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    elif mat[0][2] == mat[2][2] and mat[2][2] == mat[4][2]:
        if mat[0][2] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    elif mat[0][4] == mat[2][4] and mat[2][4] == mat[4][4]:
        if mat[0][4] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    # Horizontal
    elif mat[0][0] == mat[0][2] and mat[0][2] == mat[0][4]:
        if mat[0][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    elif mat[2][0] == mat[2][2] and mat[2][2] == mat[2][4]:
        if mat[2][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    elif mat[4][0] == mat[4][2] and mat[4][2] == mat[4][4]:
        if mat[4][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    # Diagonal
    elif mat[0][0] == mat[2][2] and mat[2][2] == mat[4][4]:
        if mat[0][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    elif mat[0][4] == mat[2][2] and mat[2][2] == mat[4][0]:
        if mat[0][4] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    else:
        for i in mat:
            for j in i:
                if j == ' ':
                    return False
                else:
                    continue
    print('Draw oh oh')
    return True


def is_valid(mat, input):
    if input != 'TL' or input != 'TM' or input != 'TR' or \
        input != 'ML' or input != 'MM' or input != 'MR' or \
            input != 'BL' or input != 'BM' or input != 'BR':
        return False
    else:
        return True


def game(mat, p1, p2):
    print('See the board below')
    display(mat)
    print('So you have to put \"TL\" for top-left, \"TM\" for top-middle, \"TR\" for top-right, "')
    while not result(mat, p1, p2):
        print(p1 + ', your turn.')
        
        while not is_valid(mat, row, col):
            in_row = input('Enter your row (left one) number: ')
            in_col = input('Enter your column (right one) number: ')
            row = int(in_row)
            col = int(in_col)
        mat[row][col] = 'O'
        display(mat)
        if result(mat, p1, p2):
            break
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
