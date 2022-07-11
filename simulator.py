from game import TicTacToeGame

tg = TicTacToeGame()

tg.init_board()
while True:
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
    if tg.check_win():
        winner = 'X' if tg.turn==0 else 'O'
        print(f"GG, {winner} wins!!") 
    tg.swap_turn()
    tg.print_board()