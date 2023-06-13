from ex00 import *
import sys


def split_booty(*wallets: dict):
    sum_gold: int = 0
    three_wallet: list = []
    for i in wallets:
        sum_gold += i.get('gold_ingots', 0)
    for i in range(3):
        three_wallet.append({'gold_ingots': int(sum_gold / 3)})
    for i in range(sum_gold % 3):
        three_wallet[i] = add_ingot(three_wallet[i])
    return three_wallet


if __name__ == '__main__':
    a = {'gold_ingots': 13, 'silver': 13, 'ingots': 10}
    b = {'ingots': 2, 'silver': 3}
    c = {'gold_ingots': 3, 'silver': 6, 'ingots': 7}
    print(split_booty(a, b, c))
