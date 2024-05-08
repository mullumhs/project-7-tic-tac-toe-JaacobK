#def main():
    # Your code goes here

#if __name__ == "__main__":
    #main()
board = []
dict = {"1A": [0,0], "A1": [0,0], "2A": [1,0], "A2": [1,0], "3A": [2,0], "A3": [2,0], "1B": [0,1], "B1": [0,1], "2B": [1,1], "B2": [1,1], "3B": [2,1], "B3": [2,1], "1C": [0,2], "C1": [0,2], "2C": [1,2], "C2": [1,2], "3C": [2,2], "C3": [2,2]}
def initilise_board():
    for i in range(3):
        board.append(["-", "-", "-"])
    display_board()

def display_board():
    print("\n  A B C")
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

def win_checking():
    wincheck = False
    if board[0][0] == board[1][0] == board[2][0] != "-":
        wincheck = True
    elif board[0][1] == board[1][1] == board[2][1] != "-":
        wincheck = True
    elif board[0][2] == board[1][2] == board[2][2] != "-":
        wincheck = True
    if board[0][0] == board[0][1] == board[0][2] != "-":
        wincheck = True
    elif board[1][0] == board[1][1] == board[1][2] != "-":
        wincheck = True
    elif board[2][0] == board[2][1] == board[2][2] != "-":
        wincheck = True
    if board[0][0] == board[1][1] == board[2][2] != "-":
        wincheck = True
    elif board[0][2] == board[1][1] == board[2][0] != "-":
        wincheck = True
    return wincheck

def win_condition():
    drawtimer = 9
    wincheck = win_checking()
    print(wincheck)
    print(drawtimer)
    if wincheck == True:
        print("you win")
    elif wincheck == False and board == [[token, token, token], [token, token, token], [token, token, token]]
            print("test")



def turn_and_place_system():
    count = 1
    while True:
        token = "X"
        if count % 2 == 0:
            token = "O"
        
        choice = (input("Where do you want to place?\n")).upper()
        while not choice == choice in dict:
            display_board()
            print("invalid choice")
            choice = (input("Where do you want to place?\n")).upper()
        while board[dict[choice][0]][dict[choice][1]] != "-":
            display_board()
            print("There is already a token there")
            choice = (input("Where do you want to place?\n")).upper()
            while not choice == choice in dict:
                display_board()
                print("invalid choice")
                choice = (input("Where do you want to place?\n")).upper()

        board[dict[choice][0]][dict[choice][1]] = token
        count += 1
        display_board()
        win_condition()



initilise_board()
turn_and_place_system()
