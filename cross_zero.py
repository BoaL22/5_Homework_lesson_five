import sys

def Numbers():

    one = '1'
    two = '2'
    tree = '3'
    four = '4'
    five = '5'
    six = '6'
    seven = '7'
    eight = '8'
    nine = '9'

                
def victory(player):
    print(f'Победили {player}! ')

def Win_one(list, player):
    one = '1'
    two = '2'
    tree = '3'
    four = '4'
    five = '5'
    six = '6'
    seven = '7'
    eight = '8'
    nine = '9'
    

    One(list, player, one, two, tree, four, five, seven, nine)
    Two(list, player, one, two, tree, five, eight)
    Tree(list, player, one, two, tree, five, six, seven, nine)
    Four(list, player, one, four, five, six, seven)
    Five(list, player, one, two, tree, four, five, six, seven, eight, nine)
    Six(list, player, tree, four, five, six, nine)
    Seven(list, player, one, tree, four, five, seven, eight, nine)
    Eigth(list, player, two, five, seven, eight, nine)
    Nine(list, player, one, tree, five, six, seven, eight, nine)

def Design(ds):
    print(f'-------------\n| {ds[0]} | {ds[1]} | {ds[2]} |\n-------------\n| {ds[3]} | {ds[4]} | {ds[5]} |\n-------------\n| {ds[6]} | {ds[7]} | {ds[8]} |\n-------------')

def motions(ds, list, play, player):

        motion = int(input(f'Ходят {player}: '))

        if motion > 0 and motion < 10:
            if str(motion) in ds:
                list.append(str(motion))
                ds[motion-1] = play
                
            else:
                print('Эта позиция уже занята! ')
                return motions(ds, list, motion, play)
        else:
            print('Введите число от 1 до 9! ')
            return motions(ds, list, motion, play)

def Game():

    ds = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    cross = 'X'
    dagger = 'крестики'
    zero = '0'
    null = 'нолики'

    crosses = []
    noughts = []

    i = 1
    while True:
        Design(ds)
        motions(ds, crosses, cross, dagger)
        i += 1
        Win_one(crosses, dagger)

        Design(ds)
        motions(ds, noughts, zero, null)
        i += 1
        Win_one(noughts, null)
        if i == 9:
            print('Ничья! ')
            break




def One(list, player, one, two, tree, four, five, seven, nine):
    if one in list:
        if two in list:
            if tree in list:
                victory(player)
                sys.exit()
                 
        elif tree in list:
            if two in list:
                victory(player)
                sys.exit()
                   
        elif five in list:
            if nine in list:
                victory(player)
                sys.exit()
                
        elif nine in list:
            if five in list:
                victory(player)
                sys.exit()
                
        elif four in list:
            if seven in list:
                victory(player)
                sys.exit()
                
        elif seven in list:
            if four in list:
                victory(player)
                sys.exit()
                
def Two(list, player, one, two, tree, five, eight):
    if two in list:
        if tree in list:
            if one in list:
                victory(player)
                sys.exit()
                
        elif one in list:
            if tree in list:
                victory(player)
                sys.exit()
                
        elif five in list:
            if eight in list:
                victory(player)
                sys.exit()
                
        elif eight in list:
            if five in list:
                victory(player)
                sys.exit()
                
def Tree(list, player, one, two, tree, five, six, seven, nine):
    if tree in list:
        if two in list:
            if one in list:
                victory(player)
                sys.exit()
                
        elif one in list:
            if two in list:
                victory(player)
                sys.exit()
                   
        elif five in list:
            if seven in list:
                victory(player)
                sys.exit()
                
        elif seven in list:
            if five in list:
                victory(player)
                sys.exit()
                
        elif six in list:
            if nine in list:
                victory(player)
                sys.exit()
                
        elif nine in list:
            if six in list:
                victory(player)
                sys.exit()
                
def Four(list, player, one, four, five, six, seven):
    if four in list:
        if one in list:
            if seven in list:
                victory(player)
                sys.exit()
                
        elif seven in list:
            if one in list:
                victory(player)
                sys.exit()
                
        elif five in list:
            if six in list:
                victory(player)
                sys.exit()
                
        elif six in list:
            if five in list:
                victory(player)
                sys.exit()
                
def Five(list, player, one, two, tree, four, five, six, seven, eight, nine):
    if five in list:
        if two in list:
            if eight in list:
                victory(player)
                sys.exit()
                
        elif eight in list:
            if two in list:
                victory(player)
                sys.exit()
                   
        elif four in list:
            if six in list:
                victory(player)
                sys.exit()
                
        elif six in list:
            if four in list:
                victory(player)
                sys.exit()
                
        elif one in list:
            if nine in list:
                victory(player)
                sys.exit()
                
        elif nine in list:
            if one in list:
                victory(player)
                sys.exit()
                
        elif seven in list:
            if tree in list:
                victory(player)
                sys.exit()
                
        elif tree in list:
            if seven in list:
                victory(player)
                sys.exit()
                
def Six(list, player, tree, four, five, six, nine):
    if six in list:
        if four in list:
            if five in list:
                victory(player)
                sys.exit()
                
        elif five in list:
            if four in list:
                victory(player)
                sys.exit()
                
        elif tree in list:
            if nine in list:
                victory(player)
                sys.exit()
                
        elif nine in list:
            if tree in list:
                victory(player)
                sys.exit()
                
def Seven(list, player, one, tree, four, five, seven, eight, nine):
    if seven in list:
        if one in list:
            if four in list:
                victory(player)
                sys.exit()
                
        elif four in list:
            if one in list:
                victory(player)
                sys.exit()
                   
        elif five in list:
            if tree in list:
                victory(player)
                sys.exit()
                
        elif tree in list:
            if five in list:
                victory(player)
                sys.exit()
                
        elif eight in list:
            if nine in list:
                victory(player)
                sys.exit()
                
        elif nine in list:
            if eight in list:
                victory(player)
                sys.exit()
                
def Eigth(list, player, two, five, seven, eight, nine):
    if eight in list:
        if two in list:
            if five in list:
                victory(player)
                sys.exit()
                
        elif five in list:
            if two in list:
                victory(player)
                sys.exit()
                
        elif seven in list:
            if nine in list:
                victory(player)
                sys.exit()
                
        elif nine in list:
            if seven in list:
                victory(player)
                sys.exit()
                
def Nine(list, player, one, tree, five, six, seven, eight, nine):
    if nine in list:
        if one in list:
            if five in list:
                victory(player)
                sys.exit()
                
        elif five in list:
            if one in list:
                victory(player)
                sys.exit()
                   
        elif tree in list:
            if six in list:
                victory(player)
                sys.exit()
                
        elif six in list:
            if tree in list:
                victory(player)
                sys.exit()
                
        elif seven in list:
            if eight in list:
                victory(player)
                sys.exit()
                
        elif eight in list:
            if seven in list:
                victory(player)
                sys.exit()


Game()
