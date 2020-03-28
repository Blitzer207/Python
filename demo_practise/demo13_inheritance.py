
class Father:
    def eat(self):
        print("Father can eat")

class Monther:
    def walk(self):
        print("walk like monther")


class son(Father,Monther):
    def eat(self):
        print("eat like son")


littleSon = son()
littleSon.eat() 
littleSon.walk()
