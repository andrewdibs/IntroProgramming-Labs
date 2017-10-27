# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Your Name Here
# Created: YYYY-MM-DD

symbol = [ " ", "x", "o" ]

def printRow(row):
    
    output = "|"
    for x in row:
        if x == 0:
            output += " " +"|"
        else:
            output += str(x) + "|"
    print(output)
    

def printBoard(board):
 
    print("+-+-+-+")
    for row in board:
        printRow(row)
        print("+-+-+-+")
        
def markBoard(board, row, col, player):
 # check to see whether the desired square is blank
    global symbol 
    if player == 1:
        mark = symbol[1]
    elif player == 2:
        mark = symbol[2]
    

    if board[row][col] == 0 :
        board[row][col] = mark

        
 # if so, set it to the player number
    


def getPlayerMove():
    row = int(input("Enter what row you would like to mark: ")) -1
    col = int(input("Enter which column you would like to mark: ")) -1# prompt the user separately for the row and column numbers
    return (row,col) # then return that row and column instead of (0,0)

def hasBlanks(board):

    for row in board:
        for num in row:
            if num == 0 :
                return True # if no square is blank, return False

    return False

def main():
    board = [[0, 0, 0]
            ,[0, 0, 0]
            ,[0, 0, 0]
        ] # TODO replace this with a three-by-three matrix of zeros
    player = 1 
    while hasBlanks(board):

        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1 # switch player for next turn
main()
