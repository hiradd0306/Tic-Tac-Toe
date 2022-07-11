from game import TicTacToeGame

tg = TicTacToeGame()

tg.init_board()
tg.show_turn()
tg.show_available_squares()
while True:
    try: 
        square = int(input("Choose a square: "))
        if square not in tg.available_squares:
            raise ValueError
    except ValueError:
        print("Please enter a valid input.\n")
    else:
        break

tg.mark_square(square)
tg.check_win()
tg.swap_turn()
tg.print_board()