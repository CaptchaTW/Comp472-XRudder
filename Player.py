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
        if self.get_pieces_counter() != 15:
            if self.board_input_checker(game, row, column):
                if game.board[row][column] == " ":
                    game.board[row][column] = self.__pieces_symbol
                    self.__pieces_counter += 1
                    return True
        else:
            print("No more tokens left to place")
            return False
        return False

    @staticmethod
    def board_input_checker(game, column, row):
        if (0 <= row < 10) and (0 <= column < 10):
            return True
        return False

    def move_piece(self, game, old_column,old_row, new_column, new_row):
        new_row, new_column = self.translate(new_column, new_row)
        old_row, old_column = self.translate(old_column, old_row)

        if new_row != old_row or new_column != old_column:
            if self.board_input_checker(game, old_row, old_column) and self.board_input_checker(game, new_row, new_column):
                if self.__pieces_symbol == game.board[old_row][old_column]:
                    if -1 <= new_row-old_row <= 1 and -1 <= new_column-old_column <= 1:
                        game.board[old_row][old_column] = " "
                        game.board[new_row][new_column] = self.__pieces_symbol
                        self.__pieces_moved_counter += 1
                        return True
        return False

    def get_pieces_counter(self):
        return self.__pieces_counter

    def get_pieces_moved_counter(self):
        return self.__pieces_moved_counter

    def get_player_symbol(self):
        return self.__pieces_symbol