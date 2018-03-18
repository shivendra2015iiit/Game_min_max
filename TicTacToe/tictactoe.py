# created by shivendra singh
'''on 02 - Nov _ 2017 '''


import numpy as np
import random
import os


board = np.ones(9)
def initialize_board():
    global board
    board= np.array([[1,1,1],[1,1,1],[1,1,1]]) # this is board I will use 1 to represent empty location 0 to represent O and 2 to represent X
#Player is O and computer is 2 or X and 1 is empty

def mapping(value):
    if value==0:
        return ("O")
    elif value ==2:
        return ("X")
    else:
        return (" ")

def print_board():

    print("\n\n  ",mapping(board[0][0]) ,"  |  " ,mapping(board[0][1]) ,"  |  ",mapping(board[0][2]) ,"\n",
          " ", mapping(board[1][0]), "  |  ", mapping(board[1][1]), "  |  ", mapping(board[1][2]), "\n",
          " ", mapping(board[2][0]), "  |  ", mapping(board[2][1]), "  |  ", mapping(board[2][2]), "\n\n")

def ismoveleft(board):
    for i in range(0,3,1):
        for j in range(0,3,1):
            if board[i][j]==1:
                return True
    return False

def win(board):

    # checking row wins
    for row in range(0,3,1):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2] :
                 if board[row][0] ==0:
                     return +10
                 elif board[row][0] == 2:
                    return -10

    # checking columns wins
    for col in range(0, 3, 1):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == 0:
                return +10
            elif board[0][col] == 2:
                return -10

     # checking diagonal wins
            if board[0][0] == board[1][1] and board[1][1] ==board[2][2] :
                if board[0][0] == 0:
                    return +10
                elif board[0][0] == 2:
                    return -10

            if board[0][2] == board[1][1] and board[1][1] == board[2][0] :
                 if board [0][2] == 0:
                     return +10
                 elif board[0][2] == 2:
                    return -10
        return 0

def minmax(board,depth,isMax):
    score = int(win(board))
    if score == 10:
        print("YOU WON")
        return
    if score == -10:
        print("YOU LOOSE")
        return
    if not ismoveleft(board):
        print("DRaW")
        return
    if(isMax):
        best =int(-1000)
        for i in range(0, 3, 1):
            for j in range(0, 3, 1):
                if board[i][j] == 1:
                    board[i][j] = 2
                    best =max(best, minmax(board, depth + 1,not isMax))
                    board[i][j] = 1
        return best
    else:
        best = int(1000)
        for i in range(0, 3, 1):
            for j in range(0, 3, 1):
                if board[i][j] == 1:
                    board[i][j] = 0
                    best = int(min(best, minmax(board, depth + 1, not isMax)))
                    board[i][j] = 1
        return best

def findbestmove(board):
    bestVal = int(-1000)
    bestrow = -1
    bestcol = -1
    returnvalue = np.array([0,0])        # this array will be returned in which first value is row then column
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            if board[i][j] == 1:
                board[i][j] = 2
                movevalue = int(minmax(board,0,False))
                board[i][j]=1

                if movevalue > bestVal:
                    bestrow = i
                    bestcol = j
                    bestVal = movevalue
    returnvalue[0]=bestrow
    returnvalue[1]=bestcol
    return returnvalue


def computerEasymove():
    moverow = int (random.randint(0,2))
    movecol = int (random.randint(0,2))
    while board[moverow][movecol] != 1:
        moverow = int(random.randint(0, 2))
        movecol = int(random.randint(0, 2))
    board[moverow][movecol] = 2



def computerMediummove():
    [moverow,movecol]=findbestmove(board)
    print(moverow)
    board[moverow][movecol] = 2

def playermove():
    move = int(input("Your Turn ENTER LOCATION(0-8) : \n"))

    while move > 8:
        print("INVALID MOVE ")
        move = int(input("Your Turn ENTER LOCATION(0-8) : \n"))

    if move <= 2:
        moverow = 0
        movecol=move%3
    elif move > 2 and move <= 5 :
        moverow = 1
        movecol = move % 3
    else:
        moverow = 2
        movecol = move % 3

    while board[moverow][movecol]!=1:
        print("INVALID MOVE ")
        move = int(input("Your Turn ENTER LOCATION(0-8) : \n"))
        while move > 8:
            print("INVALID MOVE ")
            move = int(input("Your Turn ENTER LOCATION(0-8) : \n"))

        if move  <= 2:
            moverow = 0
            movecol = move % 3
        elif move  > 2 and move  <= 5:
            moverow = 1
            movecol = move % 3
        else:
            moverow = 2
            movecol = move %3
    print(movecol)
    board[moverow][movecol]=0

def selectdifficulty():
    print("SELECT YOUR DIFFICULTY LEVEL \n"
          "1 > EASY-PEASY \n"
          "2 > MEDIUM \n"
          "3 > HARD")
    answer = int(input("\nEnter your option"))
    while answer not in [1,2,3]:
        answer = int(input("\nEnter valid option"))
    return answer




def computerHardmove():
    print_board()

def main():
    level = selectdifficulty()
    initialize_board()
    print_board()

    if level == 1 :
         while win(board)!=10 and win(board) != -10 and ismoveleft(board):
            playermove()
            print_board()
            if (ismoveleft(board)):
                if win(board) != 10 and win(board) != -10 and ismoveleft(board):
                    computerEasymove()
                    print_board()
                else:
                    break

    elif level == 2:
        while win(board) != 1:
            playermove()
            print_board()
            if win(board) != 1:
                computerMediummove()
                print_board()
            else:
                break
    else:
        while win(board) != 1:
            playermove()
            print_board()
            if win(board) != 1:
                computerHardmove()
                print_board()
            else:
                break



if __name__ == main():
     main()


