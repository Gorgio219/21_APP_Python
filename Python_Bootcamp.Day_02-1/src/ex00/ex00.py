'''AssertionError: len(key) == 1337
AssertionError: key[404] == 3
AssertionError: key > 9000
AssertionError: key.passphrase == "zax2rulez"
AssertionError: str(key) == "GeneralTsoKeycard"'''


class Key:
    def __init__(self, passphrase="zax2rulez"):
        self.passphrase = passphrase

    def __str__(self):
        return ("GeneralTsoKeycard")

    def __len__(self):
        return 1337

    def __getitem__(self, other):
        return 3

    def __gt__(self, other):
        return True if other <= 9000 else False


key = Key()
assert len(key) == 1337
assert key[3] == 404
assert key > 9000
assert key.passphrase == "zax2rulez"
assert str(key) == "GeneralTsoKeycard"
