import os
import re
import random
from copy import deepcopy 

random.seed()
random.randint(0,0)

def init_board():
    board = [[0 for i in range(8)] for j in range(8)]
    return board

def display_board(board):
    label = "\t     " 
    for i in range(8):
        label += " " + str(i+1) + "   " 
    print(label)
    for i in range(8):
        print("\t    " + " ----" * 8)
        string = "\t " + str(i+1) + " |"
        for j in range(8):
            if board[i][j] == 0:
                s = " "
            else:
                s = str(board[i][j])
            string +=  (3-len(s)) * " " + s + " |"
        print(string)
    print("\t    " + " ----" * 8)

def list_moves(board, pos):
    rx = pos[0]
    cx = pos[1] 
    kr = [-2, -2, -1, -1,  1, 1,  2, 2]
    kc = [-1,  1, -2,  2, -2, 2, -1, 1]
    moves = []
    for i in range(8):
        rn = rx + kr[i]
        cn = cx + kc[i]
        if not (rn < 1 or rn > 8 or cn < 1 or cn > 8 or board[rn-1][cn-1] != 0):
            moves.append([rn,cn])
    return moves

good = False
while not good:
    pos = input("Enter starting square r,c : ")
    if pos == 'q':
        os._exit(1)
    if re.match('[1-8],[1-8]', pos):
        pos_list = pos.split(",")
        r = int(pos_list[0])
        c = int(pos_list[1])
        good = True

game = init_board()

move_number = 1
game[r-1][c-1] = move_number
choices = 1

while move_number <= 63:
    move_number += 1
    possible_moves = list_moves(game, [r,c])
    candidate_moves = []
    move_count = []

    for m in possible_moves:
        tmpgame = deepcopy(game)
        # play_move(tmpgame, m, move_number)
        tmpgame[m[0]-1][m[1]-1] = move_number
        move_count.append(len(list_moves(tmpgame, m)))


    for i in range(len(move_count)):
        if move_count[i] == min(move_count):
            candidate_moves.append(possible_moves[i])

    move = candidate_moves[random.randint(0,len(candidate_moves)-1)]
    choices *= 2 ** (len(candidate_moves)-1)
    r = move[0]
    c = move[1]
    # play_move(game, move, move_number)
    game[r-1][c-1] = move_number
    

display_board(game)

