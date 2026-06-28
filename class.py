class Hospital:
    def __init__(self,doctors,nurses,patients,workers):
        self.doctors=doctors
        self.nurses=nurses
        self.patients=patients
        self.workers=workers

    def show(self):
        print(f"The Hospital consists {self.doctors} doctors, {self.nurses} nurses, {self.patients} patients, {self.workers} workers.")


obj = Hospital(10,20,50,25)
obj2= Hospital(5,25,67,43)
obj.show()           
obj2.show()