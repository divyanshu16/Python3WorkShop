class PowTwo:

    """
    Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.
    """
    def __init__(self, max=0):
        self.max = max

    """
    The __iter__() method returns the iterator object itself. If required, some initialization can be performed
    """
    def __iter__(self):
        self.n = 0
        return self

    """
    The __next__() method must return the next item in the sequence.
    On reaching the end, and in subsequent calls, it must raise StopIteration.
    """
    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result


def iter_check(x):
    while True:
        try:
            print(next(x))
        except StopIteration:
            print('Iteration stopped')
            break


# ob = PowTwo(2)
# iter_check(iter(ob))


def generator_1():
    """
    control as well as state it maintains
    """
    n = 1
    print('first print')
    yield n

    n += 1
    print('second print')
    yield n

    n += 1
    print('last print')
    yield n


# g1 = generator_1()
# iter_check(g1)


def generator_2(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


g2 = generator_2("Hello world")
iter_check(g2)


def generator_3(my_str):
    for i in my_str:
        yield i

#
# for char in generator_3('hello world'):
#     print(char)

