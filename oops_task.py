# Task 1

# class Student:
#     def __init__(self,name,marks):
#         self.name =name
#         self.marks =marks

#     def  display_grade(self):
#         if self.marks >= 90:
#             grade = "A"
#         elif self.marks >= 75:
#             grade = "B"
#         elif self.marks >= 55:
#             grade = "C"
#         else:
#             grade = "fail"

#         print(self.name,"Grade:", grade)

# Student1 = Student("Ashiq",99)
# Student2 = Student("Hashim",90)
# Student1.display_grade()
# Student2.display_grade()

# Task 2

class Student:
    def __init__(self,name,marks):
        self.name =name
        self.marks =marks
    def calculate_average(self):
        return sum(self.marks.values()) / len(self.marks)
    
    def  display_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 55:
            grade = "C"
        else:
            grade = "fail"

        print(self.name,"Average:", avg)
        print("grade", grade)
        


Student1 = Student("Hashim",{"Math": 80, "English": 85, "Science": 75})
Student2 = Student("Ashiq",{"Math": 80, "English": 55, "Science": 65})
Student1.display_grade()
Student2.display_grade()