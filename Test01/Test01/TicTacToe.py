#------------------------------------------------------------------------------------------------
# Tic-Tac-Toe game

def initBoard():
    board = [[0 for i in range(3)] for j in range(3)]
    return board

def displayBoard(board):
    sym = ' xo'
    print("\t    " + "  1 " + "  2 " + "  3 ")
    for i in range(3):
        print("\t    " + " ---" * 3)
        print("\t  " + str(i+1) + " | " + sym[board[i][0]] + " | " + sym[board[i][1]] + " | " + sym[board[i][2]] + " |")
    print("\t    " + " ---" * 3)

def play(board, user):
    correct = False
    while not correct:
        pos = input("Player " + str(user+1) + " move ? row,col : ")
        posList = pos.split(",")
        row = int(posList[0])-1
        col = int(posList[1])-1

        if board[row][col] == 0:
            board[row][col] = user+1
            correct = True
        else:
            print("That square %s is taken!\n" % pos)
    return board


def checkBoardForWinner(board):
    def isSame(l):
        return len(set(l)) == 1 and l[0] != 0

    for i in range(3):
        if isSame(board[i]):
            return board[i][0]

    # transpose list of lists
    board = list(map(list, zip(*game)))

    for i in range(3):
        if isSame(board[i]):
            return board[i][0]
        
    diag = [board[i][i] for i in range(3)]
    if isSame(diag):
        return diag[0]

    diag = [board[i][2-i] for i in range(3)]
    if isSame(diag):
        return diag[0]

    return 0


# Main
game = initBoard()

emptySquares = 9
winner = 0
user = 1

while emptySquares != 0 and winner == 0:
    user = 1 - user
    displayBoard(game)
    game = play(game, user)
    emptySquares-=1
    winner = checkBoardForWinner(game)

displayBoard(game)

if winner == 0:
    print("Draw!")
else:
    print("player %d wins!" % (user+1))
