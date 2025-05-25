
# Default parameters and variables

playing_board=['']*10

# Board display function
def display(board):
    print(f"{board[7]}  |  {board[8]}  |  {board[9]}")
    print(f"{board[4]}  |  {board[5]}  |  {board[6]}")
    print(f"{board[1]}  |  {board[2]}  |  {board[3]}")

# Accepting and checking user input
def player_input():
    
    # setting the marker to be initially an empty string
    marker=''

    # Running the while loop unless until the user enters the correct input then returning the assigned inputs as a tuple
    while marker != 'X' and marker != 'O':
        
        marker=input("Player 1, please enter whether to be 'X' or 'O' ").upper() 

        player1=marker

    if player1=='X':
        player2='O'
    else:
        player2='X'

    return (player1,player2)

# Placing the 'X' or 'O' in the printed matrix 
def place_marker(board,marker,position):
    board[position]=marker

# Inputing the position the player wants to choose 
def player_choice(board,marker):
    # Taking the default position to 0 ,i.e., out of the board
    chosen_position=0
    
    # Inputing the desired position from the user
    while chosen_position not in range(1,10):

        chosen_position= int(input("Enter a position between (1-9) on the board : "))

        if chosen_position not in range(1,10):
            print("Invalid input, please enter a number within range.")
        elif space_check(board,chosen_position):
            place_marker(board,marker,chosen_position)

# Checking if all three 'X' or 'O' are in line
def win_check(b):
    # if b[1]==b[2]==b[3]!='' or b[4]==b[5]==b[6]!='' or b[7]==b[8]==b[9]!='' or b[1]==b[4]==b[7]!='' or b[2]==b[5]==b[8]!='' or b[3]==b[6]==b[9]!='' or b[1]==b[5]==b[9]!='' or b[3]==b[5]==b[7]!='':
    
    for i in range(1,10,3):
        if b[i]==b[i+1]==b[i+2]!='':
            return b[i]
    for i in range(1,4):
        if b[i]==b[i+3]==b[i+6]!='':
            return b[i]
    if b[1]==b[5]==b[9]!='':
        return b[1]
    if b[3]==b[5]==b[7]!='':
        return b[3]

# checking if there is empty space in the selected positiion
def space_check(board,position):
    
    if board[position] == '':
        return True
    else:
        return False
    
print("Welcome to the game of Tic tac toe!")

p1,p2 = player_input()

turn=p1

display(playing_board)

for i in range(0,9):
    player_choice(playing_board,turn)
    
    print("Current board is :")
    
    display(playing_board)

    val=win_check(playing_board)
    if val:
        print(val+" Wins!")
        break

    if turn==p1:
        turn=p2
    else:
        turn=p1
else:
    print("The match is a tie!")