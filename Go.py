def who_won(game_board: list): # asks the user to input a list and then outputs a winner between player 1 and 2 based on the number of 1s and 2s respectively

    player1_pieces = 0 # initialize player 1 pieces counter
    player2_pieces = 0 # initialize player 2 pieces counter

    board_setup_str = input("Please type in a list of values (separated by a space) from 0-2 to create the game board. A 0 is an empty square, a 1 is Player 1's game piece, and a 2 is Player 2's game piece: ") # get user input as a string
    board_setup = board_setup_str.split() # plit the string into a list based on spaces
    board_setup = [int(element) for element in board_setup] # convert the list elements to integers (assuming the user enters integers)
    
    for element in board_setup: # loop through every element in the user input list
        if element == 1:
            player1_pieces += 1 # check if element is 1, if so, then increment player 1's pieces
        elif element == 2:
            player2_pieces += 1 # check if element is 2, if so, then increment player 2's pieces
    
    if player1_pieces == player2_pieces:
        print("Player 1 and Player 2 tie (0)") # check for tie

    elif player1_pieces > player2_pieces: 
        print("Player 1 wins (1)") # check if player 1 has more pieces

    elif player1_pieces < player2_pieces:
        print("Player 2 wins (2)") # check if player 2 has more pieces

# Testing the function
if __name__ == "__main__":
    m = [1, 2, 1, 0, 9]
    who_won(m) # Player 1 wins (1)
