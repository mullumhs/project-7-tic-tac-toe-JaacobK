
board = []
def initilise_board():
    # have the board remeber 6 of itself that later turn into rows
    for i in range(6):
        board.append(["-", "-", "-", "-", "-", "-", "-", ])
    display_board()

def display_board():
    #prints numbers for the collums
    print(" 1 2 3 4 5 6 7")
    for row in board:
        #prints a '|' at the start to make more griddy as well as well as not makeing a new line
        print("", end= '|' )
        # gets - on its own instead of '-',
        for collum in row:
            #prints a | after -
            print(collum, end= '|')
        #goes to the next row
        print()

#def Turns():


#def play():




initilise_board()

#palceing stuff
count = 1
while True:
    token = "X"
    if count % 2 == 0:
        token = "O"
    count += 1
    print (count)

    collum_choice = int(input("What Collum (1 - 7)"))
    collum_choice -= 1
    board[5][collum_choice] = token
    display_board()