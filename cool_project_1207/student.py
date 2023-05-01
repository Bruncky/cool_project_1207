from datetime import date

class Student:
    # Class attribute
    school = 'Le Wagon'

    # Initializer (constructor) method, runs when instantiated
    def __init__(self, name, age):
        self.name = name.capitalize()
        self.age = age

    # Instance method
    def says(self, something):
        print(f'{self.name} says {something}!')

    # Class method
    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name = name, age = date.today().year - birth_year)
    

# class DataStudent(Student):
#     # Class attribute
#     cursus = 'Data Science'

#     def __init__(self, name, age, batch):
#         super().__init__(name, age)

#         self.batch = batch
        

if __name__ == '__main__':
    # No inheritance
    bruno = Student(name = 'bruno', age = 29)
    tyler = Student(name = 'tyler', age = 28)
    maria = Student.from_birth_year(name = 'Maria Eduarda', birth_year = 1996)

    bruno.says('hello')
    tyler.says('hello')

    print(bruno.name, bruno.age, bruno.school)
    print(tyler.name, tyler.age, tyler.school)
    print(maria.name, maria.age, maria.school)
    # => <__main__.Student object at 0x102993820>

    # With inheritance
    # boris = DataStudent(name = 'boris', age = '35', batch = '1207')

    # print(boris.name, boris.age, boris.cursus, boris.batch)
    # print(boris.__dict__)
