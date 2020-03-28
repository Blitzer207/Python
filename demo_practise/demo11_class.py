# class Student:
#     def eat(self, name, age):
#         print(name + " can eat. " + "and he is " + age)


# Student().eat("lei", "25")


class Student():
    name = "lei"
    age = 20

    def eat(self):
        print(self.name, " can eat."+" and he is ", self.age)

    @staticmethod
    def walk():
        print("student can walk.")


Student.walk()


student1=Student()
student1.eat()
student1.walk()

student2=Student()
student2.eat()
student2.walk()