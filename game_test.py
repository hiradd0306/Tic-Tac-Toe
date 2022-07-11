from game import TicTacToeGame

tg = TicTacToeGame()

# Testing init_board()
tg.init_board()
print("Expected:")
print("|0 0 0|")
print("|0 0 0|")
print("|0 0 0|")

print("Actual:")
tg.print_board()
