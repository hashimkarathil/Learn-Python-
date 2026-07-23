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

# class Student:
#     def __init__(self,name,marks):
#         self.name =name
#         self.marks =marks
#     def calculate_average(self):
#         return sum(self.marks.values()) / len(self.marks)
    
#     def  display_grade(self):
#         avg = self.calculate_average()
#         if avg >= 90:
#             grade = "A"
#         elif avg >= 75:
#             grade = "B"
#         elif avg >= 55:
#             grade = "C"
#         else:
#             grade = "fail"

#         print(self.name,"Average:", avg)
#         print("grade", grade)
        


# Student1 = Student("Hashim",{"Math": 80, "English": 85, "Science": 75})
# Student2 = Student("Ashiq",{"Math": 80, "English": 55, "Science": 65})
# Student1.display_grade()
# Student2.display_grade()




# Task 3

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("deposited rs:" , amount)
        else:
            print("must be amount greaterthan 0.")

    def withdraw(self,amount):
        if amount <= 0:
            print("invalid amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrew Rs:", amount)
    
    def get_balance(self):
        return self.__balance
    
b1 = BankAccount("Hashim",10000)


b1.deposit(-500)
b1.withdraw(200)

print("Final Balance:", b1.get_balance())

# print(b1.__balance)

