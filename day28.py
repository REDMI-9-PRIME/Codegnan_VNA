''' LMS PORTAL '''

class Professors:
    def __init__(self, name, course, emp_id, salary):
        self.name = name
        self.course = course
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Course: {self.course}, Emp_id: {self.emp_id}, Salary: {self.salary}")


class Students:
    def __init__(self, name, course, student_id, age):
        self.name = name
        self.course = course
        self.student_id = student_id
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Course: {self.course}, Stu_id: {self.student_id}, Age: {self.age}")


class LMS:
    def __init__(self):
        self.professors = []   # use lowercase (best practice)
        self.students = []
        self.courses = {}

    # Add student
    def addStudent(self, student):
        self.students.append(student)

    # Add professor
    def addProfessor(self, professor):
        self.professors.append(professor)

    # Show students
    def showStudents(self):
        for s in self.students:
            s.display()

    # Show professors
    def showProfessors(self):
        for p in self.professors:
            p.display()


# --------- TEST ---------

lms = LMS()

p1 = Professors("Anand Rao", "Java", 101, 50000)
s1 = Students("Akash", "Python", 201, 22)

lms.addProfessor(p1)
lms.addStudent(s1)

print("\nProfessors:")
lms.showProfessors()

print("\nStudents:")
lms.showStudents()
    
