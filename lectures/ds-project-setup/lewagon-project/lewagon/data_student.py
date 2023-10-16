from lewagon.student import Student

class DataStudent(Student):
    course = 'Data Science'

    def __init__(self, name, age, batch):
        super().__init__(name, age) # calls the parent class
        self.batch = batch