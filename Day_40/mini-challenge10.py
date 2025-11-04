"""🎯 Tasks
- Create a class called Student.
- Use a constructor (__init__) to initialize:
- name (string)
- marks (integer)
- Add a method check_pass() that:
- Prints "Pass" if marks ≥ 50
- Prints "Fail" otherwise
- Create two student objects with different marks.
- Call check_pass() for each student.
"""


class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def check_pass(self):
        return f"{self.name} is Pass" if self.marks >= 50 else f"{self.name} is Fail"


student1 = Student("Yohan",89)
student2 = Student("Babu",49)
print(student1.check_pass())
print(student2.check_pass())
