import numpy as np


class Game:
    __board = None
    __rows = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    __columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

    def initialize(self):
        self.__board = np.zeros((10, 12), dtype=int)
        self.__board[0][0] = 1
        self.__board[0][1] = 2

    def print_board(self):
        print("   | ", end =' ')
        for members in self.__columns:
            print(members + "  | ", end=' ')
        counter = 0
        for columns in self.__board:
            print("\n", end='')
            print("---------------------------------------------------------------------")
            if counter !=0:
                print(self.__rows[counter], end=' ')
                print(" | ", end= ' ')
            else:
                print(self.__rows[counter], end=' ')
                print("| ", end=' ')
            counter += 1
            for rows in columns:
                print(rows, end=' ')
                print(" | ",  end=' ')