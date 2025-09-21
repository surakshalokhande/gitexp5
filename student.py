class Person:
    def display(self):
        print("I am a person.")


class Teacher(Person):
    def teach(self):
        print("I can teach.")


class Student(Person):
    def study(self):
        print("I can study.")


class SmartPerson(Teacher, Student):
    def multitask(self):
        print("I can teach and study both!")


sp = SmartPerson()


sp.display()    
sp.teach()       
sp.study()       
sp.multitask()   
