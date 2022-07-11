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

        # Win conditions
        self.win_con = [
            (1,2,3), (4,5,6), (7,8,9),
            (1,4,7), (2,5,8), (3,6,9,),
            (1,5,9), (3,5,7)
        ]

        # Players' conditions
        self.x_player_con = []
        self.o_player_con = []

        # Player turn
        self.turn = 0 # X's turn if 0, O's turn if 1

    def print_board(self):
        print(f"|{self.board[1]} {self.board[2]} {self.board[3]}|")
        print(f"|{self.board[4]} {self.board[5]} {self.board[6]}|")
        print(f"|{self.board[7]} {self.board[8]} {self.board[9]}|")

    # Create an empty board
    def init_board(self):
        for i in range(9):
            self.board[i+1] =  self.NO_MARK

    def show_available_squares(self):
        for i in self.board.keys():
            if self.board[i] is self.NO_MARK:
                self.available_squares.append(i)
        print("Availabe squares are: ")
        print(self.available_squares)

    def mark_square(self, square):
        if self.turn == 0:
            self.board[square] = self.X_MARK
            self.x_player_con.append(square)
            
        else:
            self.board[square] = self.O_MARK
            self.o_player_con.append(square)

    def check_win(self):
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
                return True     
        return False

    def show_turn(self):
        if self.turn == 0:
            print("It is X's turn.")
        else:
            print("It is O's turn.")

    def swap_turn(self):
        self.turn = 0 if self.turn==1 else 1
    



