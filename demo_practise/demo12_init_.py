class Student:

    def __init__(self,name,age):
        self.age=age
        self.name=name

    def walk(self):
        print(self.name, " can walk. ")
        print(self.name, " is ", self.age)


s1 = Student("lei","20")
s1.walk()


s2 = Student("liu","22")
s2.walk()
