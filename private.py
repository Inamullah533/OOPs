class Humans:
    __a ="ali"
    def show(self):
        print(f"My name is {self.__a}")
class Animals(Humans):
    def show2(self):
        print("Heloo")

obj = Animals()
obj.show()        
