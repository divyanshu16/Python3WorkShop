"""
https://docs.python.org/3/reference/datamodel.html#special-method-names
"""
from pymongo import MongoClient


class Family:
    # class attribute
    members = []

    # instance attribute
    def __init__(self, name, house_name, wealth):
        self.family_name = name
        self.house_name = house_name
        self.wealth = wealth

    def __str__(self):
        return 'Family with family_name {} and house_name {}'.format(self.family_name, self.house_name)

    def __repr__(self):
        return 'Family({}, {}, {})'.format(self.family_name, self.house_name, self.wealth)

    def __len__(self):
        return len(self.house_name)

    def __add__(self, other):
        return self.wealth + other.wealth

    def __lt__(self, other):
        return self.wealth < other.wealth

    @classmethod
    def add_member(cls, x):
        cls.members.append(x)

    @classmethod
    def remove_member(cls, x):
        cls.members.remove(x)

    def get_family_name(self):
        return self.family_name


family1 = Family('Rastogi', 'Rastogi_Niwas', 100)
family2 = Family('Obama', 'White House', 30)


def mongo_dunder_context_mngr():
    class MongoClientLocal:
        def __init__(self, host, port):
            print('__init__')
            self.host = host
            self.port = port

        def __enter__(self):
            print('__enter__')
            self.client = MongoClient(self.host, self.port)
            return self.client

        def __exit__(self, *args):
            print('__exit__')
            self.client.close()

    with MongoClientLocal('localhost', 27017) as client:
        print(client.Anish_DEC14.amazon_com_reviews.count())

mongo_dunder_context_mngr()
