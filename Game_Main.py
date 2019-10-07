from Game import Game
from Player import Player
def main():

    game1 = Game()
    player1 = Player("X")
    player2 = Player("O")
    game1.initialize()
    array_of_players = [player1, player2]
    while game1.get_move_counter() != 30 or player1.get_pieces_counter() !=15 or player2.get_pieces_counter()!=15:
        print(player1.get_pieces_counter())
        turn_counter = (game1.get_turn_counter()) % 2
        print("Player " + str(turn_counter+1) + " turn")
        move_choice =input("Choose your next move: \n1-Place a token \n"
              "2-Move a token\n")
        if move_choice == "1":
            put_input = input("Input which grid to place coordinates(ie:A1):\n")
            array_of_players[turn_counter].put_piece(game1, put_input[0], int(put_input[1]))
        else:
            old_move_input = input("Input which grid to move tokens(ie:A2)\n")
            new_move_input = input("Input which grid to move the token to(ie:A3)\n")
            array_of_players[turn_counter].move_piece(game1, old_move_input[0], int(old_move_input[1]), new_move_input[0],
                                                      int(new_move_input[1]))
        game1.print_board()
        game1.set_move_counter(game1.get_move_counter()+array_of_players[turn_counter].get_pieces_moved_counter())
        print("Current move counter is " + str(game1.get_move_counter()))
        print("Player " + str(turn_counter) + " Token counter is " + str(array_of_players[turn_counter].get_pieces_counter()))
        game1.set_turn_counter(game1.get_turn_counter()+1)


if __name__ == "__main__":
    main()