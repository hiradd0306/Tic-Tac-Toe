class TicTacToeGame: 
    def __init__(self):
        # Player's mark on the board
        self.X_MARK = 'X'
        self.O_MARK = 'O'
        self.NO_MARK = '-'

        # Board
        self.board = dict()
        
        # Win conditions
        self.win_con = [
            (1,2,3), (4,5,6), (7,8,9),
            (1,4,7), (2,5,8), (3,6,9,),
            (1,5,9), (3,5,7)
        ]

        # Player conditions
        self.player_con = []

    def print_board(self):
        print(f"|{self.board[1]} {self.board[2]} {self.board[3]}|")
        print(f"|{self.board[4]} {self.board[5]} {self.board[6]}|")
        print(f"|{self.board[7]} {self.board[8]} {self.board[9]}|")

    # Create an empty board
    def init_board(self):
        for i in range(9):
            self.board[i+1] =  self.NO_MARK

    def show_available_squares(self):
        available_squares = []
        for i in self.board.keys():
            if self.board[i] is self.NO_MARK:
                available_squares.append(i)
        print("Availabe squares are: ")
        print(available_squares)

    def mark_square(self, input):
        if type(input) != int:
            print("Please enter a valid integer.")
        self.board[input] = self.X_MARK
        self.player_con.append(input)

    def check_win(self):
        for con in self.win_con:
            win_con_checker = 0
            for square in con:
                if square not in self.player_con:
                    win_con_checker += 1
            if win_con_checker == 0:
                return True
        
        return False


