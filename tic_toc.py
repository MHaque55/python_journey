map = [['0:0', '0:1', '0:2'], 
        ['1:0', '1:1', '1:2'], 
        ['2:0', '2:1', '2:2']]

p1 = input('Player1, enter your name: ')
p2 = input('Player2, enter your name: ')

print(p1 + ' is \'O\'' + ' and ' + p2 + ' is \'X\'')
print('Nope you don\'t have any choice')

def display(dis_map):        
    for i in dis_map:
        for j in i:
            print(j, end = '     ')
        print()


def result(map, p1, p2):
    #Horizontal
    if(map[0][0] == map[1][0]) & (map[1][0] == map[2][0]):
        if(map[0][0]) == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True

    elif(map[0][1] == map[1][1]) & (map[1][1] == map[2][1]):
        if(map[0][1]) == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    
    elif(map[2][0] == map[2][1]) & (map[2][1] == map[2][2]):
        if(map[2][0]) == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True

    #Vertical
    elif(map[0][0] == map[0][1]) & (map[0][1] == map[0][2]):
        if(map[0][0]) == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True

    elif(map[1][0] == map[1][1]) & (map[1][1] == map[1][2]):
        if(map[1][0]) == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    
    elif(map[2][0] == map[2][1]) & (map[2][1] == map[2][2]):
        if(map[2][0]) == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True
    
    #Diagonal
    elif(map[0][0] == map[1][1]) & (map[1][1] == map[2][2]):
        if(map[0][0]) == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True

    elif(map[0][2] == map[1][1]) & (map[1][1] == map[2][0]):
        if(map[0][2]) == 'O':
            print(p1 + ' won')
        else:
            print(p2 + ' won')
        return True


    else:
        for i in map:
            for j in i:
                if (j == 'X') | (j == '0'):
                    continue
                else:
                    return False
        
    print('Draw oh oh')
    return True

def is_valid(row, col):
    if(row < 0 or row > 2) or (col < 0 or col > 2):
        print('Invalid argument, try again')
        return False
    else:
        return True

def game(map, p1, p2):
    print('See the map below')
    display(map)
    print('row : column')
    while result(map, p1, p2) != True:
        print(p1 + ', your turn.')
        in_row = input('Enter your row (left one) number: ')
        in_col = input('Enter your column (right one) number: ')
        row = int(in_row)
        col = int(in_col)
        while is_valid(row, col) == False:
            in_row = input('Enter your row (left one) number: ')
            in_col = input('Enter your column (right one) number: ')
            row = int(in_row)
            col = int(in_col)
        map[row][col] = 'O'
        display(map)
        print(p2 + ', your turn.')
        in_row = input('Enter your row (left one) number: ')
        in_col = input('Enter your column (right one) number: ')
        row = int(in_row)
        col = int(in_col)
        while is_valid(row, col) == False:
            in_row = input('Enter your row (left one) number: ')
            in_col = input('Enter your column (right one) number: ')
            row = int(in_row)
            col = int(in_col)
        map[row][col] = 'X'
        display(map)
    return True

game(map, p1, p2)







