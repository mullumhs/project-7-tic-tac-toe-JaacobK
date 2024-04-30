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
    for row in board:
        #prints a '|' at the start to make more griddy as well as well as not makeing a new line
        print("", end= '|' )
        # gets - on its own instead of '-',
        for collum in row:
            #prints a | after -
            print(collum, end= '|')
        #goes to the next row
        print()

initilise_board()

count = 1
while True:
    token = "X"
    if count % 2 == 0:
        token = "O"
    count += 1
    dict = { "1A": [0,0], "A1": [0,0], "2A": [0,1], "A1": [0,1], }
    choice = (input("Where do you want to place?\n"))
    print(dict[choice])    
    board[dict[choice][0]][dict[choice][1]] = token
    display_board()


