class Family:

    # class attribute
    visits = 0

    # instance attribute
    def __init__(self, name, house_name):
        self.family_name = name
        self.house_name = house_name
        self.members = []

    # instance method
    def add_member(self, x):
        self.members.append(x)

    # instance method
    def remove_member(self, x):
        self.members.remove(x)

    def get_family_name(self):
        return self.family_name

    def get_family_hash(self,):
        return (len(self.family_name) + 342432324) % 233


class Person(Family):
    """
    Person inherits Family Class
    """
    def __init__(self, person_name, person_age, family_name, house_name):
        super().__init__(family_name, house_name)
        self.person_name = person_name
        self.person_age = person_age

    @property
    def wealth(self):
        return 100 if self.person_age > 30 else 60

    # Polymorphism
    def get_family_name(self):
        return self.person_name.split(' ')[-1]


print("Person is subClass of Family: {}".format(issubclass(Person, Family)))

person = Person('R Jha', 24, 'Jha', 'Jha_House')

print("person is instance of Person: {}".format(isinstance(person, Person)))
# Creating variable on the fly
person.nationality = 'Indian'

# deleting the attribute
# del person.nationality

print(dir(person))
