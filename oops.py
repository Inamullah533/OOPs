class Humans:
    def __init__(self,gender,age):
        self.gender=gender
        self.age=age
   

class Animals(Humans):
    def __init__(self, gender, age,counts):
        super().__init__(gender, age)   
        self.counts=counts

    def show(self):
        print(f"The Animals is {self.gender} , Ages = {self.age} , Counts = {self.counts}")

obj =Animals("Male" , 12,20) 
obj.show()
          