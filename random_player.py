import minesweeper as ms
import random

width = 10
height = 10

games_lost = 0
games_won = 0

for x in range(100):
	board = ms.Board(10, 10, 5)
	while board.remaining_cells > 0:
		col = random.randrange(0, width)
		row = random.randrange(0, height)
		if (board.user_board[col][row] == ms.UNDISCOVERED):
			if board.discover_cell(col, row):
				print "Game lost: there were %d cells remaining." % board.remaining_cells
				games_lost += 1
				break

	if board.remaining_cells == 0:
		games_won += 1
		print "Game won."

print
print "Total games lost: %d." % games_lost
print "Total games won: %d." % games_won