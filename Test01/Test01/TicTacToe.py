#------------------------------------------------------------------------------------------------
# Tic-Tac-Toe game
import os

def init_board():
    board = [[0 for i in range(3)] for j in range(3)]
    return board

def display_board(board):
    sym = ' xo'
    print("\t    " + "  1 " + "  2 " + "  3 ")
    for i in range(3):
        print("\t    " + " ---" * 3)
        print("\t  " + str(i+1) + " | " + sym[board[i][0]] + " | " + sym[board[i][1]] + " | " + sym[board[i][2]] + " |")
    print("\t    " + " ---" * 3)

def play(board, user):
    correct = False
    while not correct:
        display_board(board)
        pos = input("Player " + str(user) + " move? row,col : ")
        if pos == 'q':
            os._exit(1)
        pos_list = pos.split(",")
        row = int(pos_list[0])-1
        col = int(pos_list[1])-1

        if board[row][col] == 0:
            board[row][col] = user
            correct = True
        else:
            print("That square [%s] is taken!\n" % pos)
    return board


def check_board_for_winner(board):
    def is_same(lst):
        return len(set(lst)) == 1 and lst[0] != 0

    # Check rows and columns
    for j in range(2):
        for i in range(3):
            if is_same(board[i]):
                return board[i][0]
        # transpose list of lists
        board = list(map(list, zip(*board)))
    
    # Check diagonals
    diag = [board[i][i] for i in range(3)]
    if is_same(diag):
        return diag[0]

    diag = [board[i][2-i] for i in range(3)]
    if is_same(diag):
        return diag[0]

    return 0


# Main
def main():
    game = init_board()
    
    empty_squares = 9
    winner = 0
    user = 1

    while empty_squares != 0 and winner == 0:
        user = 1 - user
        game = play(game, user+1)
        empty_squares-=1
        winner = check_board_for_winner(game)

    display_board(game)

    if winner == 0:
        print("Draw!")
    else:
        print("player %d wins!" % (user+1))



if __name__=="__main__":
    main()