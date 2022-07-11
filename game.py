class TicTacToeGame: 
    def __init__(self):
        # Player's mark on the board
        self.X_MARK = 'X'
        self.O_MARK = 'O'
        self.NO_MARK = '-'

        # Board
        self.board = dict()
        
        # Available Squares
        self.available_squares = []

        # All possible win conditions
        self.win_con = [
            (1,2,3), (4,5,6), (7,8,9),
            (1,4,7), (2,5,8), (3,6,9,),
            (1,5,9), (3,5,7)
        ]

        # Players' current conditions
        self.x_player_con = []
        self.o_player_con = []

        # Player turn
        self.turn = 0 # X's turn if 0, O's turn if 1

        # Game Over Flag
        self.game_over = False

    def print_board(self):
        '''Print the current board.'''
        print(f"|{self.board[1]} {self.board[2]} {self.board[3]}|")
        print(f"|{self.board[4]} {self.board[5]} {self.board[6]}|")
        print(f"|{self.board[7]} {self.board[8]} {self.board[9]}|")

    def init_board(self):
        '''Create a new board full of empty squares.'''
        for i in range(9):
            self.board[i+1] =  self.NO_MARK

    def show_available_squares(self):
        '''
        Determine which squares are available for the user to
        place a mark to. Also check for a draw if all 9 squares 
        are occupied.
        '''
        self.available_squares = []
        for i in self.board.keys():
            if self.board[i] is self.NO_MARK:
                self.available_squares.append(i)
        if len(self.available_squares) == 0:
            print("The game is a draw.")
            self.game_over = True
            return

    def mark_square(self, square):
        '''Mark a square based on which player's turn it is now.'''
        if self.turn == 0:
            self.board[square] = self.X_MARK
            self.x_player_con.append(square)
            
        else:
            self.board[square] = self.O_MARK
            self.o_player_con.append(square)

    def check_win(self):
        '''
        Check if the current player has won.
        If so, change the game over flag to True.
        '''
        for con in self.win_con:
            win_con_checker = 0
            for square in con:
                if self.turn == 0:
                    if square not in self.x_player_con:
                        win_con_checker += 1
                else:
                    if square not in self.o_player_con:
                        win_con_checker += 1
            if win_con_checker == 0:
                self.game_over = True     

    def show_turn(self):
        '''Print which player's turn it is now.'''
        if self.turn == 0:
            print("It is X's turn.")
        else:
            print("It is O's turn.")

    def swap_turn(self):
        '''Swap player's turn.'''
        self.turn = 0 if self.turn==1 else 1
    



