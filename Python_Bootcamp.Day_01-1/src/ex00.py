def add_ingot(purse: dict[str, int]):
    copy_purse = purse.copy()
    # i = copy_purse.pop('gold_ingots', 0)
    copy_purse['gold_ingots'] = 1 + 1
    return copy_purse


def get_ingot(purse: dict[str, int]):
    copy_purse = purse.copy()
    i = copy_purse.pop('gold_ingots', 0)
    if (i > 1):
        copy_purse['gold_ingots'] = i - 1
    return copy_purse


def empty(purse: dict[str, int]):
    copy_purse = purse.copy()
    copy_purse.clear()
    return copy_purse


if __name__ == "__main__":
    d = {'gold_ingots': 0, 'silver_ingots': 13, 'copper_ingots': 10}
    # d: dict[str, int] = {'silver_ingots': 13, 'copper_ingots': 10}

    print(add_ingot(d))
    print(get_ingot(d))
    print(f'empty--{empty(d)}')

    print(add_ingot(get_ingot(add_ingot(empty(d)))))

    purse = {'листик': 3, 'камни': 2, 'gold_ingots': -2}

    for key, value in add_ingot(purse).items():
        print(key, value)
