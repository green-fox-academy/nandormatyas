class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.name = 'Jane Doe'
        self.age = 30
        self.gender = 'female'
    def introduce(self):
        print('Hi, Im' + self.name + ',' + self.age + 'year old' + self.gender)
    
    def get_goal(self):
        print('My goal is to live for the moment')
class Student(Person):
    def __init__(name, age, gender, previuos_organization, skipped_days=0):
        super()__init__(name, age, gender)
        self.previuos_organization = previuos_organization
        self.skipped_days = skipped_days
        self.previous_organization = 'School of life'
    def get_goal(self):
        print('Be a junior software developer')

    def introduce(self):
        print('Hi, Im' + self.name + ',' + self.age + 'year old' + self.gender + 'from' + self.previous_organization + 'who skipped' + self.skipped_days))

    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days