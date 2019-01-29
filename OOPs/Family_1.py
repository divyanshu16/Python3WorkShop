class Family:
    """
    Family class is boilerplate for families
    """
    # class attribute
    visits = 0

    # instance attribute
    def __init__(self, name, house_name):
        self.family_name = name
        self.house_name = house_name
        self.members = []

    @classmethod
    def init_name(cls, name):
        return cls(name, name.split(' ')[-1])

    # instance method
    def add_member(self, x):
        self.members.append(x)

    # instance method
    def remove_member(self, x):
        self.members.remove(x)

    @staticmethod
    def concat(a, b):
        return a + '__' + b

    """
    whenever an object calls its method, the object itself is passed as the first argument. 
    So, ob.func() translates into MyClass.func(ob).
    """
    def get_family_name(self):
        return self.family_name


family = Family('Rastogi', 'Rastogi_Niwas')
print(family.get_family_name())


family = Family.init_name('R Rastogi')
print(family.get_family_name(), ' : ', family.house_name)
print(family.concat(family.family_name, family.house_name))

