class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    def make(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'C':
            self.state = 'A'
            return 5
        if self.state == 'E':
            self.state = 'F'
            return 8
        if self.state == 'D':
            self.state = 'H'
            return 7
        raise MealyError('make')

    def leer(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'C':
            self.state = 'E'
            return 4
        if self.state == 'E':
            self.state = 'H'
            return 9
        raise MealyError('leer')

    def load(self):
        if self.state == 'B':
            self.state = 'G'
            return 2
        if self.state == 'C':
            self.state = 'D'
            return 3
        if self.state == 'D':
            self.state = 'E'
            return 6
        if self.state == 'F':
            self.state = 'G'
            return 10
        if self.state == 'G':
            self.state = 'H'
            return 11
        raise MealyError('load')


def main():
    return StateMachine()


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.make() == 0
    assert o.leer() == 1
    assert o.make() == 5
    assert o.make() == 0
    assert o.load() == 2
    assert o.load() == 11
    o = main()
    assert o.make() == 0
    assert o.leer() == 1
    assert o.load() == 3
    assert o.make() == 7
    o = main()
    assert o.make() == 0
    assert o.leer() == 1
    assert o.load() == 3
    assert o.load() == 6
    assert o.leer() == 9
    o = main()
    assert o.make() == 0
    assert o.leer() == 1
    assert o.leer() == 4
    assert o.make() == 8
    assert o.load() == 10
    assert o.load() == 11
    raises(lambda: o.make(), MealyError)
    raises(lambda: o.load(), MealyError)
    raises(lambda: o.leer(), MealyError)
