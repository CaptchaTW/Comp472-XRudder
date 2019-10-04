from Game import Game
from Player import Player
def main():

    game1 = Game()
    player1 = Player("X")
    player2 = Player("O")
    game1.initialize()
    game1.print_board()
    print(player1.put_piece(game1, "A", 9))
    print(player2.put_piece(game1, "A", 10))
    print(player1.move_piece(game1, "A", 9, "B", 10 ))
    game1.print_board()
if __name__ == "__main__":
    main()