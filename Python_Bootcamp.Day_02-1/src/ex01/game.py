from collections import Counter
from players import *


class Game(object):

    def __init__(self, matches=8):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1: Player, player2: Player):
        for i in range(self.matches):
            if (player1.doer() and player2.doer()):
                self.registry[player1.name] += 2
                self.registry[player2.name] += 2
            elif (player1.doer() < player2.doer()):
                self.registry[player1.name] += 3
                self.registry[player2.name] -= 1
            elif (player1.doer() > player2.doer()):
                self.registry[player1.name] -= 1
                self.registry[player2.name] += 3
            else:
                pass
            print(f'{i + 1} -- {self.registry}')
            print(f'{player1.doer()}--{player2.doer()}')
            player1.check(player2)
            player2.check(player1)

    def top3(self):
        for name, score in self.registry.most_common(3):
            print(f"{name} {score}")


def main():
    game = Game()
    '''    game.play(Cheater(), Cooperator())
    game.play(Cheater(), Grudger())
    game.play(Cheater(), Copycat())
    game.play(Cheater(), Detective())
    game.play(Cooperator(), Grudger())
    game.play(Cooperator(), Copycat())
    game.play(Cooperator(), Detective())
    game.play(Grudger(), Copycat())
    game.play(Grudger(), Detective())'''
    game.play(Copycat(), Detective())

    game.top3()


if __name__ == "__main__":
    main()
