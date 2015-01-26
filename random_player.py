import minesweeper as ms
import random

class RandomPlayer(object):

	def __init__(self, height, width, num_mines, tries):
		self.width = width
		self.height = height
		self.tries = tries
		self.num_mines = num_mines

	def play(self):
		games_lost = 0
		games_won = 0

		for x in range(self.tries):
			board = ms.Board(self.height, self.width, self.num_mines)
			while board.remaining_cells > 0:
				col = random.randrange(0, self.width)
				row = random.randrange(0, self.height)
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