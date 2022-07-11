from game import TicTacToeGame

tg = TicTacToeGame()

tg.init_board()
while True:
    tg.show_available_squares()
    tg.print_board()
    if tg.game_over:
        break

    while True:
        try: 
            tg.show_turn()
            square = int(input("Choose a square number: "))
            if square not in tg.available_squares:
                raise ValueError
        except ValueError:
            print("Please enter a valid input.\n")
            tg.print_board()
        else:
            break

    tg.mark_square(square)
    print("")
    tg.check_win()
    if tg.game_over:
        winner = 'X' if tg.turn==0 else 'O'
        tg.print_board()
        print(f"GG, {winner} wins!!") 
        break
    tg.swap_turn()