d = {
    'TL': (0, 0),
    'TM': (0, 1),
    'TR': (0, 2),
    'ML': (1, 0),
    'MM': (1, 1),
    'MR': (1, 2),
    'BL': (2, 0),
    'BM': (2, 1),
    'BR': (2, 2)
}
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
    if mat[0][0] == mat[2][0] and mat[2][0] == mat[4][0] \
       and mat[0][0] != ' ':
        if mat[0][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    elif mat[0][2] == mat[2][2] and mat[2][2] == mat[4][2] \
            and mat[0][2] != ' ':
        if mat[0][2] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    elif mat[0][4] == mat[2][4] and mat[2][4] == mat[4][4] \
            and mat[0][4] != ' ':
        if mat[0][4] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    # Horizontal
    elif mat[0][0] == mat[0][2] and mat[0][2] == mat[0][4] \
            and mat[0][0] != ' ':
        if mat[0][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    elif mat[2][0] == mat[2][2] and mat[2][2] == mat[2][4] \
            and mat[2][0] != ' ':
        if mat[2][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    elif mat[4][0] == mat[4][2] and mat[4][2] == mat[4][4] \
            and mat[4][0] != ' ':
        if mat[4][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    # Diagonal
    elif mat[0][0] == mat[2][2] and mat[2][2] == mat[4][4] \
            and mat[0][0] != ' ':
        if mat[0][0] == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    elif mat[0][4] == mat[2][2] and mat[2][2] == mat[4][0] \
            and mat[0][4] != ' ':
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

def is_valid(choice, x, y):
    if choice != 'Tl' and choice != 'TM' and choice != 'TR' and \
    choice != 'ML' and choice != 'MM' and choice != 'MR' and \
    choice != 'BL' and choice != 'BM' and choice != 'BR':
        

def game(pos, mat, p1, p2):
    print('TL, TM, TR, ML, MM, MR, BL, BM, BR')
    print()
    display(mat)
    print()
    while not result(map, p1, p2):
        print(p1 + ', your turn')
        choice = input('Choose place:')
        x, y = pos[choice]
        while not is_valid(choice, x, y):
            

    

