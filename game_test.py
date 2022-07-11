from game import TicTacToeGame

tg = TicTacToeGame()

# Testing init_board()
print("Testing init_board():")
tg.init_board()
print("Expected:")
print("|- - -|")
print("|- - -|")
print("|- - -|")

print("Actual:")
tg.print_board()

# Testing show_available_squares()
print("\nTesting show_available_squares():")
print("All 9 squares should be available, as no marks have been placed.")
tg.show_available_squares()

# Testing mark_sqaure()
print("\nTesting mark_sqaure():")
print("After marking the square 3, there should be a X mark.")
tg.mark_square(3)
tg.print_board()
print("Now, there should be 8 available squares, 1-9 except 3.")
tg.show_available_squares()

# Testing check_win()
print("\nTesting check_win():")
print("Right now, no players have won, thus the game should continue.")
print("Expected:\nThe game continues.")
print("Actual:")
if tg.check_win():
    print("The game is over, someone won!")
else:
    print("The game continues.")

tg.mark_square(5)
tg.mark_square(7)
print("After placing X marks on square 5 and 7, the game should be over.")
tg.print_board()
print("Expected:\nThe game is over, someone won!")
print("Actual:")
if tg.check_win():
    print("The game is over, someone won!")
else:
    print("The game continues.")