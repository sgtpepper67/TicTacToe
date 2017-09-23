#!/usr/bin/python3

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

play = 'y'
counter = 2
while(play == 'y'):
	print("PLAYER " + str(counter % 2 + 1) + ": Where do you want to place your piece:")
	placement = int(input()) - 1
	if (board[placement] != 'X' or 'O'):	
		if(counter % 2 == 0):
			board[placement] = 'X'
		elif(counter % 2 == 1):
			board[placement] = 'O'
	elif(board[placement] == 'X' or 'O'):
		print("That spot is taken!")
	
	print(board[0:3])
	print(board[3:6])
	print(board[6:9])
	
	if(board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8]):
		print("Horizontal win by player " + str(counter % 2 + 1))
		play = ''
	elif(board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8]):
		print("Vertical win by player " + str(counter % 2 + 1))
		play = ''
	elif(board[0] == board[4] == board[8] or board[2] == board[4] == board[6]):
		print("Diagonal win by player " + str(counter % 2 + 1))
		play = ''

	counter += 1
