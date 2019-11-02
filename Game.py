import numpy as np
from Player import Player
import math

class Game:
    board = None
    __rows = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    __columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    __move_counter = 0
    __turn_counter = 0
    __AI_turn = 0

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

    def set_move_counter(self, total_move):
        self.__move_counter = total_move

    def get_move_counter(self):
        return self.__move_counter

    def get_turn_counter(self):
        return self.__turn_counter

    def set_turn_counter(self, turn_counter ):
        self.__turn_counter = turn_counter

    def check_winning_conditions(self,player, column, row):
        row, column = Player.translate(column, row)
        # middle
        if player.board_input_checker(self, column+1,row+1) and player.board_input_checker(self, column+1,row-1) \
                and player.board_input_checker(self, column-1,row-1)and player.board_input_checker(self, column-1,row+1):
            if self.board[row+1][column+1] == player.get_player_symbol():
                if self.board[row+1][column-1] == player.get_player_symbol():
                    if self.board[row-1][column+1] == player.get_player_symbol():
                        if self.board[row-1][column-1] == player.get_player_symbol():
                            if self.board[row][column+1] == " " or self.board[row][column+1] \
                                    == player.get_player_symbol() or\
                                    self.board[row][column-1] == " " or \
                                    self.board[row][column-1] == player.get_player_symbol():
                                return True
        # top-right
        if player.board_input_checker(self, column-2,row) and player.board_input_checker(self, column-1,row+1) \
                and player.board_input_checker(self, column-2,row+2)and player.board_input_checker(self, column,row+2):
            if self.board[row][column-2] == player.get_player_symbol():
                if self.board[row+1][column-1] == player.get_player_symbol():
                    if self.board[row+2][column-2] == player.get_player_symbol():
                        if self.board[row+2][column] == player.get_player_symbol():
                            if (self.board[row+1][column] == " " or self.board[row+1][column]
                                == player.get_player_symbol()) or ( self.board[row+1][column-2]
                                                                     == " " or self.board[row+1][column-2]
                                                                     == player.get_player_symbol()):
                                return True
        # top left
        if player.board_input_checker(self, column,row+2) and player.board_input_checker(self, column+1,row+1) \
                and player.board_input_checker(self, column+2,row)and player.board_input_checker(self, column+2,row+2):
            if self.board[row+2][column] == player.get_player_symbol():
                if self.board[row+1][column+1] == player.get_player_symbol():
                    if self.board[row][column+2] == player.get_player_symbol():
                        if self.board[row+2][column+2] == player.get_player_symbol():
                            if (self.board[row+1][column] == " " or self.board[row+1][column] ==
                                player.get_player_symbol()) or ( self.board[row+1][column+2]
                                                                  == " " or self.board[row+1][column-2]
                                                                  == player.get_player_symbol()):
                                return True
        # bottom left
        if player.board_input_checker(self, column, row - 2) and player.board_input_checker(self, column + 1, row - 1) \
                and player.board_input_checker(self, column + 2, row) and player.board_input_checker(self, column + 2,
                                                                                                     row - 2):
            if self.board[row-2][column] == player.get_player_symbol():
                if self.board[row-1][column+1] == player.get_player_symbol():
                    if self.board[row][column + 2] == player.get_player_symbol():
                        if self.board[row-2][column + 2] == player.get_player_symbol():
                            if (self.board[row -1][column] == " " or self.board[row - 1][column] ==
                                player.get_player_symbol()) or (self.board[row - 1][column + 2]
                                                                == " " or self.board[row - 1][column - 2]
                                                                == player.get_player_symbol()):
                                return True
        #bottom right
        if player.board_input_checker(self, column, row - 2) and player.board_input_checker(self, column -1, row - 1) \
                and player.board_input_checker(self, column - 2, row) and player.board_input_checker(self, column - 2,
                                                                                                     row - 2):
            if self.board[row - 2][column] == player.get_player_symbol():
                if self.board[row - 1][column - 1] == player.get_player_symbol():
                    if self.board[row][column -2] == player.get_player_symbol():
                        if self.board[row-2][column -2] == player.get_player_symbol():
                            if (self.board[row - 1][column] == " " or self.board[row - 1][column] ==
                                player.get_player_symbol()) or (self.board[row - 1][column - 2]
                                                                == " " or self.board[row - 1][column - 2]
                                                                == player.get_player_symbol()):
                                return True
        return False

    def check_move_winning(self,player, column, row):
        row,column = player.translate(column,row)
        if player.board_input_checker(self, column, row - 1) and player.board_input_checker(self, column - 2, row - 1) \
                and player.board_input_checker(self, column , row+1) and player.board_input_checker(self, column - 2,
                                                                                                     row +1):
            if self.board[row][column-2] == player.get_player_symbol():
                if self.board[row+1][column] != " " and self.board[row+1][column] != player.get_player_symbol():
                    if self.board[row -1][column] != " " and self.board[row -1][column] != player.get_player_symbol():
                        if self.board[row  -1][column-2] != " " and self.board[row  -1][column-2] \
                                != player.get_player_symbol():
                            if self.board[row + 1][column - 2] != " " and self.board[row + 1][column - 2] \
                                    != player.get_player_symbol():
                                if self.board[row][column - 1] != " " and self.board[row ][column - 1] \
                                        != player.get_player_symbol():
                                    return True
        if player.board_input_checker(self, column, row - 1) and player.board_input_checker(self, column + 2, row - 1) \
                and player.board_input_checker(self, column, row + 1) and player.board_input_checker(self, column + 2,
                                                                                                     row + 1):
            if self.board[row][column + 2] == player.get_player_symbol():
                if self.board[row + 1][column] != " " and self.board[row + 1][column] != player.get_player_symbol():
                    if self.board[row - 1][column] != " " and self.board[row - 1][column] != player.get_player_symbol():
                        if self.board[row - 1][column + 2] != " " and self.board[row - 1][column + 2] \
                                != player.get_player_symbol():
                            if self.board[row + 1][column + 2] != " " and self.board[row + 1][column + 2] \
                                    != player.get_player_symbol():
                                if self.board[row][column + 1] != " " and self.board[row][column + 1] \
                                        != player.get_player_symbol():
                                    return True
        return False

    def scoring(self,array_player, columns, rows):
        score2 = 0
        turn_counter_ = self.__turn_counter % 2
        if self.check_winning_conditions(array_player[turn_counter_], columns, rows):
            if turn_counter_ == self.__AI_turn:
                score2 = 1000
            else:
                score2 = -1000
            return score2

        for i in range(10):
            for j in range(8):
                counter_AI = 0
                counter_human = 0
                if self.board[j][i] == array_player[turn_counter_].get_player_symbol():
                    counter_AI += 1
                elif self.board[j][i] == array_player[(self.__turn_counter+1)%2].get_player_symbol():
                    counter_human += 1
                if self.board[j][i+2] == array_player[turn_counter_].get_player_symbol():
                    counter_AI += 1
                elif self.board[j][i+2] == array_player[(self.__turn_counter + 1) % 2].get_player_symbol():
                    counter_human += 1
                if self.board[j+1][i+1] == array_player[turn_counter_].get_player_symbol():
                    counter_AI += 1
                elif self.board[j+1][i+1] == array_player[(self.__turn_counter + 1) % 2].get_player_symbol():
                    counter_human += 1
                if self.board[j+2][i] == array_player[turn_counter_].get_player_symbol():
                    counter_AI += 1
                elif self.board[j+2][i] == array_player[(self.__turn_counter + 1) % 2].get_player_symbol():
                    counter_human += 1
                if self.board[j+2][i+2] == array_player[turn_counter_].get_player_symbol():
                    counter_AI += 1
                elif self.board[j+2][i+2] == array_player[(self.__turn_counter + 1) % 2].get_player_symbol():
                    counter_human += 1
                if counter_human == 0:
                    score2 += math.pow(counter_AI,3)

                if counter_AI == 0:
                    score2 -= math.pow(counter_human,3)

        if turn_counter_ != self.__AI_turn:
            score2 = -score2
        return score2


    def minimax_function(self, array_player, depth):
        global score1
        score1 =0
        score = None
        turn_counter_ = self.__turn_counter % 2
        if turn_counter_ == self.__AI_turn:
            score = -10001
        else:
            score = +10001
        column_holder = None
        row_holder = None
        move_column_holder = None
        move_row_holder = None
        movetype = None
        for columns in self.__columns:
            for rows in self.__rows:
                holder_board = np.copy(self.board)
                if array_player[turn_counter_].put_piece(self, columns, rows):
                    array_player[turn_counter_].set_pieces_counter(
                        array_player[turn_counter_].get_pieces_counter() - 1)
                    if depth !=1:
                        self.__turn_counter+=1
                        column_holder1,row_holder1,new_column_holder,new_row_holder,score1,movetype= self.minimax_function(array_player,depth-1)
                        self.__turn_counter-=1
                        print(score, score1)
                        if turn_counter_ == self.__AI_turn:
                            if score < score1:
                                print(columns,rows)
                                column_holder, row_holder = columns, rows
                                score = score1
                                movetype = "Put"
                        else:
                            if score > score1:
                                column_holder, row_holder = columns, rows
                                score = score1
                                movetype = "Put"

                    else:

                        if turn_counter_ == self.__AI_turn:
                            if score < self.scoring(array_player, columns, rows):
                                column_holder, row_holder = columns, rows
                                score = self.scoring(array_player, columns, rows)
                                movetype = "Put"

                        else:
                            if score > self.scoring(array_player, columns, rows):
                                column_holder, row_holder = columns, rows
                                score = self.scoring(array_player, columns, rows)
                                movetype = "Put"
                self.board = holder_board
                if self.__move_counter != 30:
                    if self.board[10-rows][ord(columns.lower()) - 97] == array_player[turn_counter_].get_player_symbol():
                        holder_board = np.copy(self.board)
                        if array_player[turn_counter_].move_piece(self, columns, rows, chr(ord(columns) - 1), rows - 1):
                            array_player[turn_counter_].set_pieces_moved_counter(
                                array_player[turn_counter_].get_pieces_moved_counter() - 1)
                            if depth != 1:
                                self.__turn_counter += 1
                                column_holder1, row_holder1,new_column_holder1,new_row_holder1,score1,movetype = self.minimax_function(array_player, depth - 1)
                                self.__turn_counter -= 1
                                if turn_counter_ == self.__AI_turn:
                                    if score < score1:
                                        column_holder, row_holder,move_column_holder,move_row_holder = columns, rows,chr(ord(columns)-1),rows-1
                                        score = score1
                                        movetype = "Move"

                                else:
                                    if score > score1:
                                        column_holder, row_holder,move_column_holder,move_row_holder = columns, rows,chr(ord(columns)-1),rows-1
                                        score = score1
                                        movetype = "Move"

                            else:

                                if turn_counter_ == self.__AI_turn:
                                    if score < self.scoring(array_player, chr(ord(columns)-1), rows-1):
                                        column_holder, row_holder,move_column_holder,move_row_holder = columns, rows,chr(ord(columns)-1),rows-1
                                        score = self.scoring(array_player, chr(ord(columns)-1), rows-1)
                                        movetype = "Move"

                                else:
                                    if score > self.scoring(array_player, chr(ord(columns)-1), rows-1):
                                        column_holder, row_holder,move_column_holder,move_row_holder = columns, rows,chr(ord(columns)-1),rows-1
                                        score = self.scoring(array_player, chr(ord(columns)-1), rows-1)
                                        movetype = "Move"

                        self.board = holder_board
                        holder_board = np.copy(self.board)

                        if array_player[turn_counter_].move_piece(self, columns, rows, chr(ord(columns) - 1) , rows):
                            array_player[turn_counter_].set_pieces_moved_counter(
                                array_player[turn_counter_].get_pieces_moved_counter() - 1)
                            if depth != 1:
                                self.__turn_counter += 1
                                column_holder1, row_holder1,new_column_holder1,new_row_holder1,score1,movetype = self.minimax_function(array_player, depth - 1)
                                self.__turn_counter -= 1
                                print(score, score1)
                                if turn_counter_ == self.__AI_turn:
                                    if score < score1:
                                        column_holder, row_holder,move_column_holder,move_row_holder = columns, rows,chr(ord(columns)-1),rows
                                        score = score1
                                        movetype = "Move"

                                else:
                                    if score > score1:
                                        column_holder, row_holder,move_column_holder,move_row_holder = columns, rows,chr(ord(columns)-1),rows
                                        score = score1
                                        movetype = "Move"

                            else:

                                if turn_counter_ == self.__AI_turn:
                                    if score < self.scoring(array_player, chr(ord(columns)-1), rows):
                                        column_holder, row_holder,move_column_holder,move_row_holder = columns, rows,chr(ord(columns)-1),rows
                                        score = self.scoring(array_player, chr(ord(columns)-1), rows)
                                        movetype = "Move"

                                else:
                                    if score > self.scoring(array_player, chr(ord(columns)-1), rows):
                                        column_holder, row_holder,move_column_holder,move_row_holder = columns, rows,chr(ord(columns)-1),rows
                                        score = self.scoring(array_player, chr(ord(columns)-1), rows)
                                        movetype = "Move"

                        self.board = holder_board
                        holder_board = np.copy(self.board)

                        if array_player[turn_counter_].move_piece(self, columns, rows, chr(ord(columns) - 1), rows + 1):
                            array_player[turn_counter_].set_pieces_moved_counter(
                                array_player[turn_counter_].get_pieces_moved_counter() - 1)
                            if depth != 1:
                                self.__turn_counter += 1
                                column_holder1, row_holder1,new_column_holder1,new_row_holder1,score1,movetype = self.minimax_function(array_player, depth - 1)
                                self.__turn_counter -= 1
                                print(score, score1)
                                if turn_counter_ == self.__AI_turn:
                                    if score < score1:
                                        column_holder, row_holder,move_column_holder,move_row_holder = columns, rows,chr(ord(columns)-1),rows+1
                                        score = score1
                                        movetype = "Move"

                                else:
                                    if score > score1:
                                        column_holder, row_holder,move_column_holder,move_row_holder = columns, rows,chr(ord(columns)-1),rows+1
                                        score = score1
                                        movetype = "Move"

                            else:

                                if turn_counter_ == self.__AI_turn:
                                    if score < self.scoring(array_player, chr(ord(columns)-1), rows+1):
                                        column_holder, row_holder,move_column_holder,move_row_holder = columns, rows,chr(ord(columns)-1),rows+1
                                        score = self.scoring(array_player, chr(ord(columns)-1), rows+1)
                                        movetype = "Move"

                                else:
                                    if score > self.scoring(array_player, chr(ord(columns)-1), rows+1):
                                        column_holder, row_holder,move_column_holder,move_row_holder = columns, rows,chr(ord(columns)-1),rows+1
                                        score = self.scoring(array_player, chr(ord(columns)-1), rows+1)
                                        movetype = "Move"
                        self.board = holder_board
                        holder_board = np.copy(self.board)

                        if array_player[turn_counter_].move_piece(self, columns, rows, columns, rows - 1) :
                            array_player[turn_counter_].set_pieces_moved_counter(
                                array_player[turn_counter_].get_pieces_moved_counter() - 1)
                            if depth != 1:
                                self.__turn_counter += 1
                                column_holder1, row_holder1, new_column_holder1, new_row_holder1, score1,movetype = self.minimax_function(
                                    array_player, depth - 1)
                                self.__turn_counter -= 1
                                print(score, score1)
                                if turn_counter_ == self.__AI_turn:
                                    if score < score1:
                                        column_holder, row_holder, move_column_holder, move_row_holder = columns, rows, columns, rows - 1
                                        score = score1
                                        movetype = "Move"

                                else:
                                    if score > score1:
                                        column_holder, row_holder, move_column_holder, move_row_holder = columns, rows, columns , rows - 1
                                        score = score1
                                        movetype = "Move"

                            else:

                                if turn_counter_ == self.__AI_turn:
                                    if score < self.scoring(array_player, columns , rows -1):
                                        column_holder, row_holder, move_column_holder, move_row_holder = columns, rows, columns , rows - 1
                                        score = self.scoring(array_player, columns , rows -1)
                                        movetype = "Move"

                                else:
                                    if score > self.scoring(array_player, columns , rows -1):
                                        column_holder, row_holder, move_column_holder, move_row_holder = columns, rows, columns , rows - 1
                                        score = self.scoring(array_player, columns , rows - 1)
                                        movetype = "Move"

                        self.board = holder_board
                        holder_board = np.copy(self.board)

                        if array_player[turn_counter_].move_piece(self, columns, rows, columns, rows + 1) :
                            array_player[turn_counter_].set_pieces_moved_counter(
                                array_player[turn_counter_].get_pieces_moved_counter() - 1)
                            if depth != 1:
                                self.__turn_counter += 1
                                column_holder1, row_holder1, new_column_holder1, new_row_holder1, score1,movetype = self.minimax_function(
                                    array_player, depth - 1)
                                self.__turn_counter -= 1
                                print(score, score1)
                                if turn_counter_ == self.__AI_turn:
                                    if score < score1:
                                        column_holder, row_holder, move_column_holder, move_row_holder = columns, rows, columns, rows + 1
                                        score = score1
                                        movetype = "Move"

                                else:
                                    if score > score1:
                                        column_holder, row_holder, move_column_holder, move_row_holder = columns, rows, columns , rows + 1
                                        score = score1
                                        movetype = "Move"

                            else:

                                if turn_counter_ == self.__AI_turn:
                                    if score < self.scoring(array_player, columns , rows + 1):
                                        column_holder, row_holder, move_column_holder, move_row_holder = columns, rows, columns, rows + 1
                                        score = self.scoring(array_player, columns , rows + 1)
                                        movetype = "Move"

                                else:
                                    if score > self.scoring(array_player, columns , rows + 1):
                                        column_holder, row_holder, move_column_holder, move_row_holder = columns, rows, columns, rows + 1
                                        score = self.scoring(array_player, columns , rows + 1)
                                        movetype = "Move"

                        self.board = holder_board
                        holder_board = np.copy(self.board)

                        if array_player[turn_counter_].move_piece(self, columns, rows, chr(ord(columns) + 1), rows - 1):
                            array_player[turn_counter_].set_pieces_moved_counter(
                                array_player[turn_counter_].get_pieces_moved_counter() - 1)
                            self.board = holder_board
                            if depth != 1:
                                self.__turn_counter += 1
                                column_holder1, row_holder1, new_column_holder1, new_row_holder1, score1,movetype = self.minimax_function(
                                    array_player, depth - 1)
                                self.__turn_counter -= 1
                                print(score, score1)
                                if turn_counter_ == self.__AI_turn:
                                    if score < score1:
                                        column_holder, row_holder, move_column_holder, move_row_holder = columns, rows, chr(ord(columns)+1), rows - 1
                                        score = score1
                                        movetype = "Move"

                                else:
                                    if score > score1:
                                        column_holder, row_holder, move_column_holder, move_row_holder = columns, rows, chr(ord(columns)+1), rows - 1
                                        score = score1
                                        movetype = "Move"

                            else:

                                if turn_counter_ == self.__AI_turn:
                                    if score < self.scoring(array_player, chr(ord(columns)+1), rows - 1):
                                        column_holder, row_holder, move_column_holder, move_row_holder = columns, rows, chr(ord(columns)+1), rows - 1
                                        score = self.scoring(array_player, chr(ord(columns)+1), rows - 1)
                                        movetype = "Move"

                                else:
                                    if score > self.scoring(array_player, chr(ord(columns)+1) ,rows - 1):
                                        column_holder, row_holder, move_column_holder, move_row_holder = columns, rows, chr(ord(columns)+1), rows - 1
                                        score = self.scoring(array_player, chr(ord(columns)+1), rows - 1)
                                        movetype = "Move"

                        self.board = holder_board
                        holder_board = np.copy(self.board)

                        if array_player[turn_counter_].move_piece(self, columns, rows, chr(ord(columns) + 1), rows):
                            array_player[turn_counter_].set_pieces_moved_counter(
                                array_player[turn_counter_].get_pieces_moved_counter() - 1)
                            if depth != 1:
                                self.__turn_counter += 1
                                column_holder1, row_holder1, new_column_holder1, new_row_holder1, score1,movetype = self.minimax_function(
                                    array_player, depth - 1)
                                self.__turn_counter -= 1
                                print(score, score1)
                                if turn_counter_ == self.__AI_turn:
                                    if score < score1:
                                        column_holder, row_holder, move_column_holder, move_row_holder = columns, rows, chr(ord(columns)+1), rows
                                        score = score1
                                        movetype = "Move"

                                else:
                                    if score > score1:
                                        column_holder, row_holder, move_column_holder, move_row_holder = columns, rows, chr(ord(columns)+1), rows
                                        score = score1
                                        movetype = "Move"

                            else:

                                if turn_counter_ == self.__AI_turn:
                                    if score < self.scoring(array_player, chr(ord(columns)+1), rows ):
                                        column_holder, row_holder, move_column_holder, move_row_holder = columns, rows, chr(ord(columns)+1), rows
                                        score = self.scoring(array_player, chr(ord(columns)+1), rows )
                                        movetype = "Move"

                                else:
                                    if score > self.scoring(array_player, chr(ord(columns)+1), rows ):
                                        column_holder, row_holder, move_column_holder, move_row_holder = columns, rows, chr(ord(columns)+1), rows
                                        score = self.scoring(array_player, chr(ord(columns)+1), rows )
                                        movetype = "Move"

                        self.board = holder_board
                        holder_board = np.copy(self.board)
                        if array_player[turn_counter_].move_piece(self, columns, rows, chr(ord(columns) + 1), rows + 1):
                            array_player[turn_counter_].set_pieces_moved_counter(
                                array_player[turn_counter_].get_pieces_moved_counter() - 1)
                            if depth != 1:
                                self.__turn_counter += 1
                                column_holder1, row_holder1, new_column_holder1, new_row_holder1, score1,movetype = self.minimax_function(
                                    array_player, depth - 1)
                                self.__turn_counter -= 1
                                print(score, score1)
                                if turn_counter_ == self.__AI_turn:
                                    if score < score1:
                                        column_holder, row_holder, move_column_holder, move_row_holder = columns, rows, chr(ord(columns)+1), rows + 1
                                        score = score1
                                        movetype = "Move"

                                else:
                                    if score > score1:
                                        column_holder, row_holder, move_column_holder, move_row_holder = columns, rows, chr(ord(columns)+1), rows + 1
                                        score = score1
                                        movetype = "Move"

                            else:

                                if turn_counter_ == self.__AI_turn:
                                    if score < self.scoring(array_player, chr(ord(columns)+1), rows + 1):
                                        column_holder, row_holder, move_column_holder, move_row_holder = columns, rows, chr(ord(columns)+1), rows + 1
                                        score = self.scoring(array_player, chr(ord(columns)+1), rows + 1)
                                        movetype = "Move"

                                else:
                                    if score > self.scoring(array_player, chr(ord(columns)+1), rows + 1):
                                        column_holder, row_holder, move_column_holder, move_row_holder = columns, rows, chr(ord(columns)+1), rows + 1
                                        score = self.scoring(array_player, chr(ord(columns)+1), rows + 1)
                                        movetype = "Move"

                        self.board = holder_board



        return column_holder, row_holder,move_column_holder,move_row_holder, score,movetype

    def set_AI_turn(self,number):
        self.__AI_turn = number
    def get_AI_turn(self):
        return self.__AI_turn


