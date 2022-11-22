# main function of the mini project Tic Tac Toe

def display_board(position):
    print("***************")
    print("* "+position[0][0]+"|"+position[0][1]+"|"+position[0][2]+" *")
    print("* ---|---|--- *")
    print("* "+position[1][0]+"|"+position[1][1]+"|"+position[1][2]+" *")
    print("* ---|---|--- *")
    print("* "+position[2][0]+"|"+position[2][1]+"|"+position[2][2]+" *")
    print("***************")
    

def player_input(player):
    print("Player "+ player +"'s turn...")
    row = int(input("Enter row: "))
    column = int(input("Enter column: "))
    return row, column
    
        
def check_win(position, playerValue):
    for row in range(3):
        win = True
        for column in range(3):
            if position[row][column] != playerValue:
                win = False
        if win:
            return win
    
    for row in range(3):
        win = True
        for column in range(3):
            if position[column][row] != playerValue:
                win = False
        if win:
            return win
    
    win = True
    for row in range(3):
        if position[row][row] != playerValue:
            win = False
    if win:
        return win
    
    win = True
    for row in range(3):
        if position[row][3 - 1 - row] != playerValue:
            win = False
            break
    if win:
        return win
    

print("Welcome to the TIC TAC TOE!!")
position = [["   ","   ","   "], ["   ","   ","   "], ["   ","   ","   "]]
display_board(position)
for turn in range(1,10):
    if turn%2 == 0:
        player = 'X'
        [row, column] = player_input(player)
        while (row > 3 or column > 3 or position[row-1][column-1] != '   '):
            if row > 3 or column > 3:
                print("Row and column should be smaller than 3")
                print("Try again")
            if position[row-1][column-1] == ' X ' or position[row-1][column-1] == ' O ' :
                print("try another position")
            [row, column] = player_input(player)
        position[row-1][column-1] = ' X '
        display_board(position)
        result = check_win(position, ' X ')
        if result:
            print('X is the winner!!')
            break
    else:
        player = 'O'
        [row, column] = player_input(player)
        while (row > 3 or column > 3 or position[row-1][column-1] != '   '):
            if row > 3 or column > 3:
                print("Row and column should be smaller than 3")
                print("Try again")
            if position[row-1][column-1] == ' X ' or position[row-1][column-1] == ' O ' :
                print("try another position")
            [row, column] = player_input(player)
        position[row-1][column-1] = ' O '
        display_board(position)
        result = check_win(position, ' O ')
        if result:
            print('O is the winner!!')
            break


