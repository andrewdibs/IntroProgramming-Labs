# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Your Name Here
# Created: YYYY-MM-DD

symbol = [ " ", "x", "o" ]

def printRow(row):
    
    output = "|"
    for x in row:
        output += str(x) + "|"
    print(output)
    

def printBoard(board):
 
    print("+-+-+-+")
    for row in board:
        printRow(row)
        print("+-+-+-+")
        
def markBoard(board, row, col, player):
 # check to see whether the desired square is blank
 # if so, set it to the player number
    pass
def getPlayerMove():
    input("") # prompt the user separately for the row and column numbers
    return (0,0) # then return that row and column instead of (0,0)
def hasBlanks(board):
 # for each row in the board...
 # for each square in the row...
 # check whether the square is blank
 # if so, return True
    return True # if no square is blank, return False
def main():
    board = [] # TODO replace this with a three-by-three matrix of zeros
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1 # switch player for next turn
main()
