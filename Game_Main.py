from Game import Game
from Player import Player
def main():
    game1 = Game()
    player1 = Player("X")
    game1.initialize()
    game1.print_board()
    player1.put_piece(game1, "Z", 10)
    game1.print_board()
if __name__ == "__main__":
    main()