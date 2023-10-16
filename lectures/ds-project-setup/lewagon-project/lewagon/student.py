from datetime import date

class Student:
    school = 'Le Wagon'
    # DATA
    # name, age
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    # instance method
    def says(self, something):
        print(f'{self.name} says "{something}"')

    @classmethod # you don't need an instance to use it
    def from_birth_year(cls, name, birth_year):
        age = date.today().year - birth_year
        return cls(name, age)


