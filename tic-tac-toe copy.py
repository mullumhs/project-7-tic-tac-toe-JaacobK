def main():
    # Your code goes here
    
    dict = {"1A": [0,0], "A1": [0,0], "2A": [1,0], "A2": [1,0], "3A": [2,0], "A3": [2,0], "1B": [0,1], "B1": [0,1], "2B": [1,1], "B2": [1,1], "3B": [2,1], "B3": [2,1], "1C": [0,2], "C1": [0,2], "2C": [1,2], "C2": [1,2], "3C": [2,2], "C3": [2,2]}
    intro()
    board = initilise_board()
    game()

def intro():
    #prints an intro message to the player.
    print("Welcome to Tic Tac Toe".center(256," "))

def initilise_board():
    board = []
    #Adds ["-", "-", "-"] to board 3 times makeing board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    for i in range(3):
        board.append(["-", "-", "-"])
    #Calls the function display_board() 
    return board

def reset_board(board):
    #Clears the board makeing it [] again.
    board.clear()

def display_board():
    #Prints A B C on the top of the grid.
    print("\n  A B C")
    i = 0
    for row in board:
        #prints a '|' at the start of each row to make it more of a grid shape as well as puts 1, 2, 3 on the side of the grid by + 1 to i and printing out the answer 3 times.
        i += 1
        print(i, end= '|' )
        #Makes - on its own instead of '-'
        for collum in row:
            #Prints a | after every - to also make a grid shape
            print(collum, end= '|')
        #goes to the next row
        print()

def win_checking():
    wincheck = False
    #Checks the coordinates of each collum to see if there is 3 tokens in a row and if there is it makes wincheck = True.
    if board[0][0] == board[1][0] == board[2][0] != "-":
        wincheck = True
    elif board[0][1] == board[1][1] == board[2][1] != "-":
        wincheck = True
    elif board[0][2] == board[1][2] == board[2][2] != "-":
        wincheck = True
    #Checks the coordinates of each row to see if there is 3 tokens in a row and if there is it makes wincheck = True.
    if board[0][0] == board[0][1] == board[0][2] != "-":
        wincheck = True
    elif board[1][0] == board[1][1] == board[1][2] != "-":
        wincheck = True
    elif board[2][0] == board[2][1] == board[2][2] != "-":
        wincheck = True
    #Checks the coordinates of each diagonal to see if there is 3 tokens in a row and if there is it makes wincheck = True.
    if board[0][0] == board[1][1] == board[2][2] != "-":
        wincheck = True
    elif board[0][2] == board[1][1] == board[2][0] != "-":
        wincheck = True
    #Lets wincheck be used in other functions when called.
    return wincheck

def draw_checking(board):
#Calls the win_checking() function to see what wincheck =
    wincheck = win_checking()
    #Searches through every element in board to see if there is a '-' left and is False if there is and True if there is not.
    for row in board:
        for collum in row:
            if collum == '-':
                #Lets draw_checking(board) be called to see if it true of false. (True if it ran to here.) (Also means no draw.)
                return False
    #Runs if there are no '-' left and makes sure the last move wasn't a winning move with the else return false after.
    if wincheck == False:
        return True
    else:
        return False

def turn_and_place_system():
    count = 1
    loop = True
    #Makes a loop
    while loop == True:
        token = "X"
        #Checks to see if it is even and if it O's turn if not it is X's turn.
        if count % 2 == 0:
            token = "O"
        #lets the player type their move and turns their awnser into capitals. (So 3a turns to 3A.)
        choice = (input("Where do you want to place?\n")).upper()
        #checks if the players choice was in the dict showing calling display_board() to print out the board again and makeing them type a valid move until they do
        while not choice == choice in dict:
            display_board()
            print("invalid choice")
                #lets the player type their move and turns their awnser into capitals.
            choice = (input("Where do you want to place?\n")).upper()
            #Checks if the spot the player is placing doesn't allready have a token and prints out the board again and makes them type a valid move until they do.
        while board[dict[choice][0]][dict[choice][1]] != "-":
            display_board()
            print("There is already a token there")
                #lets the player type their move and turns their awnser into capitals.
            choice = (input("Where do you want to place?\n")).upper()
            #checks if the players choice was in the dict showing calling display_board() to print out the board again and makeing them type a valid move until they do
            while not choice == choice in dict:
                display_board()
                print("invalid choice")
                    #lets the player type their move and turns their awnser into capitals.
                choice = (input("Where do you want to place?\n")).upper()
        #Links up the choice to the key in dict that it is and then gets the values form that key and places a token in that spot.
        board[dict[choice][0]][dict[choice][1]] = token
        #+ 1 to the count to make it the next persons turn.
        count += 1
        #Calls the display_board() function to print out the board
        display_board()
        #Calls the win_checking() function to see what wincheck = and if it == true. It also turns loop off so it no longer repeats and lets token be used in other functions when called.
        wincheck = win_checking()
        if wincheck == True:
            loop == False
            return token
        #Calls draw_checking(board) to see if it is falls meaning the game is tied. (Checks wincheck incase someone wins on last move.) It also turns loop off so it no longer repeats and lets token be used in other functions when called.
        elif wincheck == False and draw_checking(board) == True:
            loop == False
            return token
                
def game():
    #Calls the turn_and_place_system() to strart the game and get the token when it finishes
    token = turn_and_place_system()
    #Checks if there was no draw at the end of the game (meaning someone won) and congratulates the winner.
    if draw_checking(board) == False:
        if token == "X":
            print("X's win")
        elif token == "O":
            print("O's win")
        #Lets the player choice if they want to play again or quit.
        play_again = (input("Do you wish to play again?\nType 1 if yes\nType 2 if no\n"))
        #Makes sure the player typed a number, making them keep typing until they do so as well as turning the number into an integer.
        while not play_again.isdigit():
            print("Please type 1 or 2")
            play_again = (input("Do you wish to play again?\nType 1 if yes\nType 2 if no\n"))
        play_again = int(play_again)
        #Makes sure the player typed a number between 1 and 2.
        while play_again < 1 or play_again > 2:
            print("Please type 1 or 2")
            play_again = (input("Do you wish to play again?\nType 1 if yes\nType 2 if no\n"))
            #Makes sure the player typed a number, making them keep typing until they do so as well as turning the number into an integer.
            while not play_again.isdigit():
                print("Please type 1 or 2")
                play_again = (input("Do you wish to play again?\nType 1 if yes\nType 2 if no\n"))
            play_again = int(play_again)
        #If the player wants to restart it calls all those functions causeing the game to restart.
        if play_again == 1:
            reset_board()
            intro()
            initilise_board()
            game()
        #Leaves no more code to run causeing the game to stop.
        if play_again == 2:
            print("Thankyou for playing")
    #Checks if there was  draw at the end of the game and tells the players it was a draw.
    elif draw_checking(board) == True:
        print("Draw")
        #Lets the player choice if they want to play again or quit
        play_again = (input("Do you wish to play again?\nType 1 if yes\nType 2 if no\n"))
        #Makes sure the player typed a number, making them keep typing until they do so as well as turning the number into an integer.
        while not play_again.isdigit():
            print("Please type 1 or 2")
            play_again = (input("Do you wish to play again?\nType 1 if yes\nType 2 if no\n"))
        play_again = int(play_again)
        #Makes sure the player typed a number between 1 and 2.
        while play_again < 1 or play_again > 2:
            print("Please type 1 or 2")
            play_again = (input("Do you wish to play again?\nType 1 if yes\nType 2 if no\n"))
            #Makes sure the player typed a number, making them keep typing until they do so as well as turning the number into an integer.
            while not play_again.isdigit():
                print("is it here")
                print("Please type 1 or 2")
                play_again = (input("Do you wish to play again?\nType 1 if yes\nType 2 if no\n"))
            play_again = int(play_again)
        #If the player wants to restart it calls all those functions causeing the game to restart.
        if play_again == 1:
            reset_board()
            intro()
            initilise_board()
            game()
        #Leaves no more code to run causeing the game to stop.
        if play_again == 2:
            print("Thankyou for playing.")
                
    #Calls all those function to make the game start.


if __name__ == "__main__":
    main()
