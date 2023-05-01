from cool_project_1207.student import Student

class DataStudent(Student):
    # Class attribute
    cursus = 'Data Science'

    def __init__(self, name, age, batch):
        super().__init__(name, age)

        self.batch = batch

if __name__ == '__main__':
    boris = DataStudent(name = 'boris', age = '35', batch = '1207')

    print(boris.name, boris.age, boris.cursus, boris.batch)

    print(boris.__dict__)