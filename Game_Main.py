from Game import Game
from Player import Player
import sys

def main():

    game1 = Game()
    player1 = Player("X")
    player2 = Player("O")
    game1.initialize()
    array_of_players = [player1, player2]
    while game1.get_move_counter() != 30 or player1.get_pieces_counter() != 15 or player2.get_pieces_counter() != 15:
        turn_counter = (game1.get_turn_counter()) % 2
        print("Player " + str(turn_counter+1) + " turn")
        if game1.get_move_counter() == 15 and array_of_players[turn_counter] == 15:
            print("No more options left")
            game1.set_turn_counter(game1.get_turn_counter() + 1)
            continue
        while True:
            move_choice = input("Choose your next move: \n1-Place a token \n"
                  "2-Move a token\n")
            if move_choice == "1":
                if array_of_players[turn_counter].get_pieces_counter() == 15:
                    print("No more tokens to place")
                    continue
                while True:
                        put_input = input("Input which grid to place coordinates(ie:A1):\n")
                        try:
                            while not array_of_players[turn_counter].put_piece(game1, put_input[0], int(put_input[1:])):
                                print("Invalid Inputs, Please Try Again")
                                put_input = input("Input which grid to place coordinates(ie:A1):\n")
                        except:
                            print("Invalid Inputs, Please try again")
                        else:
                            if game1.check_winning_conditions(array_of_players[turn_counter],put_input[0],int(put_input[1:])):
                                print(game1.print_board())
                                print("Player " + str(turn_counter+1) + " is the Winner")
                                sys.exit(0)
                            break
                break
            elif move_choice == "2":
                if game1.get_move_counter() == 30:
                    print("No moves left for both players")
                    continue
                if array_of_players[turn_counter].get_pieces_counter() == 0:
                    print("No pieces available to be moved")
                    continue
                while True:
                    old_move_input = input("Input which grid to move tokens(ie:A2)\n")
                    new_move_input = input("Input which grid to move the token to(ie:A3)\n")
                    try:
                        while not array_of_players[turn_counter].move_piece(game1, old_move_input[0], int(old_move_input[1:]), new_move_input[0],
                                                          int(new_move_input[1:])):
                            print("Invalid Input, Please Try Again")
                            old_move_input = input("Input which grid to move tokens(ie:A2)\n")
                            new_move_input = input("Input which grid to move the token to(ie:A3)\n")
                    except:
                        print("Invalid Input, Please try again")
                    else:
                        break
                break
            else:
                print("Invalid Input, please choose a valid option")
        game1.print_board()
        game1.set_move_counter(game1.get_move_counter()+array_of_players[turn_counter].get_pieces_moved_counter())
        print("Current move counter is " + str(game1.get_move_counter()))
        print("Player " + str(turn_counter) + " Token counter is " + str(array_of_players[turn_counter].get_pieces_counter()))
        game1.set_turn_counter(game1.get_turn_counter()+1)


if __name__ == "__main__":
    main()