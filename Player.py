
class Player:
    __total_move_counter = None

    def __init__(self,symbol):
        self.__pieces_counter = 0
        self.__pieces_symbol = symbol

    @staticmethod
    def translate(column, row):
        column = ord(column.lower())-97
        row = row-10
        return row, column

    def put_piece(self, game, column, row):
        row, column = Player.translate(column, row)
        game.board[row][column] = self.__pieces_symbol

