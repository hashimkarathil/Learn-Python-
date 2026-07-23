# ..............Python Classes and Objects.................


class Car:
    def __init__(self, make, model,year):
        self.make= make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")



# my_car = Car("Toyota","Corolla",2021) # Creating an object (instance) of the Car class

# my_car.display_info()    # Accessing object methods


# Objects in Python.....

# car1 = Car("Honda","Civic",2022)
# car2 = Car("Ford","Mustang",2023)

# car1.display_info()
# car2.display_info()

# ...........................


# The "Self" keyword............

# class Person:
#     def __init__(self,name,age):
#         self.name =name
#         self.age = age

#     def greet(self):
#         print(f"Hello, my name is {self.name} and i am {self.age} years old.")

# Person1 = Person("Alice",30)
# Person1.greet()

# .......................


#  Accessing Class Attributes and Methods

# class Dog:
#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name= name
        
#     def brak(self):
#         print(f"{self.name} says woof!")


# dog1 = Dog("Labrador","Buddy") # Creating an object

# print(dog1.breed)   # Accessing attributes

# dog1.brak()  # Accessing methods

# class Person:
#     def __init__(self, name, age,Qualification):
#         self.name= name
#         self.age = age
#         self.Qualification = Qualification

#     def display_info(self):
#         print(f"My Name is {self.name},my age  is {self.age} year old and Qualification is {self.Qualification}")
    
    
# Person1 = Person("Hashim",24,"MCA")
# # Person1.display_info()
# print(Person1.name)
# Person1.display_info()


# The __str__() Method


# class Book:
#     def __init__(self,title,author):
#         self.title =title
#         self.author = author

    
#     def __str__(self):
#         return f"'{self.title} by {self.author}"

# book = Book("1984","George Orwell")
# print(book)


# 8. Class Variables vs Instance Variables.....


# class Employee:
#     company = "ABC Corp" 

#     def __init__(self, name, position):
#         self.name = name 
#         self.position = position 

# emp1 = Employee("John", "Manager")
# emp2 = Employee("Alice", "Developer")

# # Accessing class variable
# print(emp1.company) 
# print(emp2.company) 

# # Accessing instance variable
# print(emp1.name) 
# print(emp2.name) 

# print(emp1.position) 
# print(emp2.position) 


# .....................................................................

# ...............................................................
# : OOP Notes Inner Class, Composition, Tight vs Loose Coupling :
# ...............................................................

# 1. Inner Class......

# class Employee:
#     class Company:
#         def __init__(self,cname,location):
#             self.cname = cname
#             self.location= location
#     def __init__(self,name,salary,cname,location):
#         self.name= name
#         self.salary = salary
#         self.Company = Employee.Company(cname, location) # inner class object

        
#     def display_employee(self):
#         print(f"Name:{self.name}, Salary: {self.salary},Company:{self.Company.cname}, Location:{self.Company.location}")

# emp = Employee("John",50000,"XYZ Crop","London")
# emp.display_employee()



# 2 Tightly Coupled Composition.....


# class Company:
#     def __init__(self,cname,location):
#         self.cname= cname
#         self.location = location

# class Employee:
#     def __init__(self,name,salary,cname,location):
#         self.name =name
#         self.salary = salary
#         self.company =Company(cname, location)

#     def display_employee(self):
#         print(f"Name: {self.name}, Salary: {self.salary}, Company: {self.company.cname}, Location: {self.company.location}")

# emp = Employee("John",50000,"XYZ Crop","London")
# emp.display_employee()



# 3.   Loose Coupling

# class Company:
#     def __init__(self, cname, location):
#          self.cname = cname
#          self.location = location
# class Employee:
#     def __init__(self, name, position, comp): 
#         self.name = name
#         self.position = position
#         self.comp = comp
#     def display_employee(self):
#         print(f"Name: {self.name}, Position: {self.position}, Company: {self.comp.cname}, Location: {self.comp.location}")

# c1 = Company("ABC Corp", "New York")
# emp = Employee("John Doe", "Manager", c1) #injected
# emp.display_employee()




# ..............Encapulation.................................


# class Employee:
#     def __init__(self,name,salary):
#         self.name = name    #public attribute
#         self.__salary = salary   # private attribute
    
#     def display_employee(self):
#         print(f"Name: {self.name}, Salary: {self.__salary}")
    
#     def update_salary(self, new_salary):
#         self.__salary += new_salary


# emp = Employee("john", 50000)
# emp.display_employee()


# emp.update_salary(10000)
# emp.display_employee()