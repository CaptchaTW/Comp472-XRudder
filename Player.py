class Player:
    __total_move_counter = None

    def __init__(self, symbol):
        self.__pieces_counter = 0
        self.__pieces_symbol = symbol
        self.__pieces_moved_counter = 0

    @staticmethod
    def translate(column, row):
        column = ord(column.lower()) - 97
        row = 10 - row
        return row, column

    def put_piece(self, game, column, row):
        row, column = Player.translate(column, row)
        if self.board_input_checker(game, row, column):
            game.board[row][column] = self.__pieces_symbol
            return True
        return False

    @staticmethod
    def board_input_checker(game, column, row):
        if (0 <= row < 10) and (0 <= column < 10):
            if game.board[row][column] == " ":
                return True
        return False

    # def move_piece(self, game, piece_position, new_position ):

    def get_pieces_counter(self):
        return self.__pieces_counter

    def get_pieces_moved_counter(self):
        return self.__pieces_moved_counter
