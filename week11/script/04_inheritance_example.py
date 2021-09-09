class Person(object):
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def introduction(self):
        print(f'name: {self.name}, age: {self.age}, gender: {self.gender}')


class Teacher(Person):
    def __init__(self, position: str, *args, **kwargs):
        super(Teacher, self).__init__(*args, **kwargs)
        self.position = position

    def introduction(self):
        print("I'm teacher.")

    def my_position(self):
        print(f'my position is : {self.position}')


t = Teacher(name='aaa', age=40, gender='man', position='1 class teacher')
t.introduction()
t.my_position()