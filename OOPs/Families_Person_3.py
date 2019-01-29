class Family:

    # class attribute
    visits = 0
    members = []

    # instance attribute
    def __init__(self, name, house_name):
        self.family_name = name
        self.house_name = house_name

    # instance method
    def get_family_name(self):
        return self.family_name

    # instance method
    def get_family_hash(self,):
        return (len(self.family_name) + 342432324) % 233

    @classmethod
    def get_members(cls):
        return len(cls.members)

    @classmethod
    def add_member(cls, x):
        cls.members.append(x)

    @classmethod
    def remove_member(cls, x):
        cls.members.remove(x)


class Office:
    members_count = 0

    def __init__(self, office_name):
        self.office_name = office_name
        Office.members_count += 1

    @classmethod
    def get_members(cls):
        return cls.members_count


class Person(Office, Family):
    """
    Person inherits Family Class
    """
    def __init__(self, person_name, person_age, family_name, house_name, office_name):
        Office.__init__(self, office_name)
        Family.__init__(self, family_name, house_name)
        self.person_name = person_name
        self.person_age = person_age

    @property
    def wealth(self):
        return 100 if self.person_age > 30 else 60

    # Polymorphism
    def get_family_name(self):
        return self.person_name.split(' ')[-1]


print("Person is subClass of Family: {}".format(issubclass(Person, Family)))

person = Person('R Jha', 24, 'Jha', 'Jha_House', 'xCompany')

print("person is instance of Person: {}".format(isinstance(person, Person)))
# Creating variable on the fly
person.nationality = 'Indian'

# deleting the attribute
# del person.nationality
