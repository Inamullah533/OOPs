class Humans:
    a = "Inamullah"

    def show1(self):
        print (f"My name is {self.a} ")

class Animals(Humans):
    def show(self):
        print("I am animal")


obj = Animals()
obj.show1()