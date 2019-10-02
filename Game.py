import numpy as np


class Game:
    board = None
    __rows = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    __columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

    def initialize(self):
        self.board = np.zeros((10, 12), dtype=str)
        for i in range(0,len(self.board)):
            for j in range(0,len(self.board[i])):
                self.board[i][j]=" "
        print("X-Rudder Game Begins")

    def print_board(self):
        print("   | ", end =' ')
        for members in self.__columns:
            print(members + "  | ", end=' ')
        counter = 0
        for columns in self.board:
            print("\n", end='')
            print("----------------------------------------------------------------------------")
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