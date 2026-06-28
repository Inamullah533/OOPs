class BSCS:
    def __init__(self,teachers,students,sections,subjects):
        self.teachers=teachers
        self.students=students
        self.sections=sections
        self.subjects=subjects
    def show(self):
        print(f"BSCS consists {self.teachers} teachers , {self.students} students , {self.sections} sections, and {self.subjects} subjects")


class BSIT(BSCS):  
    def __init__(self, teachers, students, sections, subjects):
        super().__init__(teachers, students, sections, subjects)

obj = BSCS(20,50,2,6)
obj2= BSIT(20,67,2,7)     
obj.show()   
obj2.show()