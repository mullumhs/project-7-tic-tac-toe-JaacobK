#def main():
    # Your code goes here

#if __name__ == "__main__":
    #main()
board = []
def initilise_board():
    for i in range(3):
        board.append(["-", "-", "-"])
    display_board()

def display_board():
    print(" A B C")
    i = 0
    for row in board:
        #prints a '|' at the start to make it more of a grid shape as well as not makeing a new line
        i += 1
        print(i, end= '|' )
        # gets - on its own instead of '-',
        for collum in row:
            #prints a | after -
            print(collum, end= '|')
        #goes to the next row
        print()

def horizontalwincheck():
    if board[0][0] == board[1][0] == board[2][0] != "-":
        wincheck = True
    elif board[0][1] == board[1][1] == board[2][1] != "-":
        wincheck = True
    elif board[0][2] == board[1][2] == board[2][2] != "-":
        wincheck = True

def Verticalwincheck():
    if board[0][0] == board[0][1] == board[0][2] != "-":
        wincheck = True
    elif board[1][0] == board[1][1] == board[1][2] != "-":
        wincheck = True
    elif board[2][0] == board[2][1] == board[2][2] != "-":
        wincheck = True

def Diagonalwincheck():
    if board[0][0] == board[1][1] == board[2][2] != "-":
        wincheck = True
    elif board[0][2] == board[1][1] == board[2][0] != "-":
        wincheck = True

def wincondition():
    wincheck = False
    horizontalwincheck()
    Verticalwincheck()
    Diagonalwincheck()
    if wincheck == True:
        print 

def turn_and_place_system():
    count = 1
    while True:
        token = "X"
        if count % 2 == 0:
            token = "O"
        count += 1
        dict = { "1A": [0,0], "A1": [0,0], "2A": [0,1], "A2": [0,1], "3A": [0,2], "A3": [0,2], "1B": [1,0], "B1": [1,0],  "2B": [1,1], "B2": [1,1], "3B": [1,2], "B3": [1,2], "1C": [2,0], "C1": [2,0], "2C": [2,1], "C2": [2,1], "3C": [2,2], "C3": [2,2]}
        choice = (input("Where do you want to place?\n"))
        print(choice)
        print(dict[choice])    
        board[dict[choice][0]][dict[choice][1]] = token
        display_board()

initilise_board()
turn_and_place_system()