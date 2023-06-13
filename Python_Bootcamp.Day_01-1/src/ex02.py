def decor_function(obj):
    def wrapper(purse: dict):
        print("SQUEAK")
        return (obj(purse))
    return wrapper


@decor_function
def add_ingot(purse: dict[str, int]):
    copy_purse = purse.copy()
    i = copy_purse.pop('gold_ingots', 0)
    copy_purse['gold_ingots'] = 1 + i
    return copy_purse


@decor_function
def get_ingot(purse: dict[str, int]):
    copy_purse = purse.copy()
    i = copy_purse.pop('gold_ingots', 0)
    if (i > 1):
        copy_purse['gold_ingots'] = i - 1
    return copy_purse


@decor_function
def empty(purse: dict[str, int]):
    copy_purse = purse.copy()
    copy_purse.clear()
    return copy_purse


if __name__ == "__main__":
    a = {'gold_ingots': 10, 'silver': 13, 'ingots': 10}

    add_ingot(a)
    print(add_ingot(a))
    print(get_ingot(a))
    print(empty(a))
'''
    print(add_ingot(get_ingot(add_ingot(empty(d)))))

    purse = {'листик': 3, 'камни': 2, 'gold_ingots': -2}

    for key, value in add_ingot(purse).items():
        print(key, value)
'''
