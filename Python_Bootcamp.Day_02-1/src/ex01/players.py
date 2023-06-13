class Player:
    def __init__(self, name: str = None, do: bool = True):
        self.name = name
        self.do = do

    def doer(self):
        return (0 if self.do == False else 1)

    def check(self, other):
        pass


class Cheater(Player):
    def __init__(self):
        super().__init__(name='Cheater', do=False)


class Cooperator(Player):
    def __init__(self):
        super().__init__(name='Cooperator')


class Copycat(Player):
    def __init__(self):
        super().__init__(name='Copycat')

    def check(self, other):
        self.do = other.do


class Grudger(Player):
    def __init__(self):
        super().__init__(name='Grudger')

    def check(self, other):
        if (not (other.doer())):
            self.do = False


class Detective(Player):
    def __init__(self):
        super().__init__(name='Detective', do=False)
        self.match = 4
        self.flag = 0

    def doer(self):
        if (self.match):

            return (1 if self.match != 3 else 0)
        return (0 if self.do == False else 1)

    def check(self, other):
        if (self.match):
            if (other.doer() == 0 and self.flag != 1):
                self.flag = 1
            print(f'SM-{self.match} {self.flag} {self.do} return = {self.doer()}')
            self.match -= 1
        else:
            if (self.flag):
                self.do = other.do
            else:
                pass
