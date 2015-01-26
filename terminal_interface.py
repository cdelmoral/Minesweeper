import minesweeper as ms

print "Let's play Minesweeper..."

(height, width) = (0, 0)
while height < 1 or height > 99:
	try:
		height = int(raw_input("How many cells tall should be your board? "))
	except ValueError:
		print "It should be a number between 1 and 99, let me ask you again..."

while width < 1 or width > 99:
	try:
		width = int(raw_input("How about the width? "))
	except ValueError:
		print "It should be a number between 1 and 99, I'll give you another try..."

num_mines = 0
while num_mines < 1 or num_mines > (height * width) - 1:
	try:
		num_mines = int(raw_input("Your board has a total of %d cells. How many of them should have a mine? " % (height * width)))
	except ValueError:
		print "Read carefully..."

board = ms.Board(height, width, num_mines)
board.play_user()