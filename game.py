class TicTacToeGame: 
    def __init__(self):
        # Player's mark on the board
        self.X_MARK = 1
        self.O_MARK = 2
        self.NO_MARK = 0

        # Board
        self.board = dict()

    def print_board(self):
        print(f"|{self.board[1]} {self.board[2]} {self.board[3]}|")
        print(f"|{self.board[4]} {self.board[5]} {self.board[6]}|")
        print(f"|{self.board[7]} {self.board[8]} {self.board[9]}|")

    def init_board(self):
        for i in range(9):
            self.board[i+1] =  self.NO_MARK

    def place_mark(self):
        available_squares = []
        for i in len(self.board):
            if self.board[i+1] != self.NO_MARKS:
                available_squares.append(i+1)
# Create an empty board


