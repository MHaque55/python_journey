mat = [[' ', '|', ' ', '|', ' '],
       ['-', '+', '-', '+', '-'],
       [' ', '|', ' ', '|', ' '],
       ['-', '+', '-', '+', '-'],
       [' ', '|', ' ', '|', ' ']]

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
    if mat[0][0] == mat[2][0] and mat[2][0] == mat[4][0] and mat[0][0] != ' ':
        if mat[0][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    elif mat[0][2] == mat[2][2] and mat[2][2] == mat[4][2] and mat[0][2] != ' ':
        if mat[0][2] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    elif mat[0][4] == mat[2][4] and mat[2][4] == mat[4][4] and mat[0][4] != ' ':
        if mat[0][4] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    # Horizontal
    elif mat[0][0] == mat[0][2] and mat[0][2] == mat[0][4] and mat[0][0] != ' ':
        if mat[0][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    elif mat[2][0] == mat[2][2] and mat[2][2] == mat[2][4] and mat[2][0] != ' ':
        if mat[2][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    elif mat[4][0] == mat[4][2] and mat[4][2] == mat[4][4] and mat[4][0] != ' ':
        if mat[4][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    # Diagonal
    elif mat[0][0] == mat[2][2] and mat[2][2] == mat[4][4] and mat[0][0] != ' ':
        if mat[0][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    elif mat[0][4] == mat[2][2] and mat[2][2] == mat[4][0] and mat[0][4] != ' ':
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
    if input == 'TL' or input == 'TM' or input == 'TR' or \
        input == 'ML' or input == 'MM' or input == 'MR' or \
            input == 'BL' or input == 'BM' or input == 'BR':
        return True
    else:
        return False


def get_input():
    place = input('Where do you want to put your mark? ')
    return place


def placement(mat, mark, input):
    if input == 'TL':
        mat[0][0] = mark
    elif input == 'TM':
        mat[0][2] = mark
    elif input == 'TR':
        mat[0][4] = mark
    elif input == 'ML':
        mat[2][0] = mark
    elif input == 'MM':
        mat[2][2] = mark
    elif input == 'MR':
        mat[2][4] = mark
    elif input == 'BL':
        mat[4][0] = mark
    elif input == 'BL':
        mat[4][2] = mark
    elif input == 'BR':
        mat[4][4] = mark


def game(mat, p1, p2):
    print('See the board below')
    print()
    display(mat)
    print()
    print('This is how you put your input')
    print('Top-Left == \"TL\", Top-Middle = \"TM\", Top-Right = \"TR\"')
    print('Middle-Left = \"ML\", Center = \"MM\", Middle-Right = \"MR\"')
    print('Bottom-Left = \"BL\", Bottom-Mid = \"BM\", Bottom-Right = \"BR\"')
    print()
    while not result(mat, p1, p2):
        print(p1 + ', your turn.')
        input = get_input()
        while not is_valid(mat, input):
            input = get_input()
        placement(mat, 'O', input)
        display(mat)
        if result(mat, p1, p2):
            break
        print(p2 + ', your turn.')
        input = get_input()
        while not is_valid(mat, input):
            input = get_input()
        placement(mat, 'X', input)
        display(mat)
    return True


game(mat, p1, p2)
