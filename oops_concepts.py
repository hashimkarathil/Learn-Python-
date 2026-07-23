#  .....................OOP Concepts..............



# ..............Inheritance.............
# Single Inheritance....

# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound")

# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} says Woof")
# dog = Dog("buddy")
# dog.speak()


# Multiple Inheritance............

# class Engine:
#     def start_engine(self):
#         print("Engine started")

# class Wheels:
#     def rotate(self):
#         print("Wheels are rotatig")

# class Car(Engine, Wheels):
#     def drive(self):
#         print("Car is driving")


# car = Car()
# car.start_engine()
# car.rotate()
# car.drive()





# Multilevel Inheritance........

# class Grandparent:
#     def sing(self):
#         print("parent is dancing")

# class Parent(Grandparent):
#     def dance(self):
#         print("Parent is dancing")

# class Child(Parent):
#     def dance(self):
#         print("child is playing")


# child = Child()
# child.sing()
# child.dance()
# child.dance()

# Hierarchical Inheritance..........


# class Animal:
#     def speak(self):
#         print("Animal speaks")


# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")


# class Cat(Animal):
#     def speak(self):
#         print("Cat meows")


# dog = Dog()
# cat = Cat()

# dog.speak()
# cat.speak()





# Hybrid Inheritance...........


# class A:
#     def method_a(self):
#         print("method from class A")

# class B(A):
#     def method_b(self):
#         print("method from class B")

# class C(A):
#     def method_c(self):
#         print("method from class C")
    
# class D(B,C):
#     def method_d(self):
#         print("method from class D")


# d = D()
# d.method_a() 
# d.method_b() 
# d.method_c() 
# d.method_d() 




# Polymorphism...........



# class Animal:
#     def speak(self):
#         return "some sound"
    
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# def animal_sound(animal: Animal):
#     return animal.speak()

# dog =Dog()
# cat = Cat()
# print(animal_sound(dog))
# print(animal_sound(cat))


# Method Overriding

# class Animal:
#     def speak(self):
#         print("animal makes a sound")


# class Dog(Animal):
#     def speak(self):
#         print("dog says woof")

# class Cat(Animal):
#     def speak(self):
#         print("dog says meow")

# animals = [Dog(),Cat()]

# for animal in animals:
#     animal.speak()


# Duck Typing..............


# class Dog:
#     def speak(self):
#         print("Woof!")
# class Cat:
#     def speak(self):
#         print("Meow!")
# class Human:
#     def speak(self):
#         print("Hello!")

# def make_it_speak(obj):
#     obj.speak()

# for creature in [Dog(),Cat(),Human()]:
#     make_it_speak(creature)



# Abstraction.................


# from abc import ABC, abstractmethod


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass


# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# rectangle = Rectangle(10,20)
# print(rectangle.area())


# Constructor and Destructor...........

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print(f"{self,name} has been created")

#     def __del__(self):
#         print(f"{self.name} has been destroyed")

# p1 = Person("John",30)
# del p1






#  ..............Decorator................................

# def deco(func):
#     def wrapper():
#         print("added sprinklers")
#         func()
#         print("finished icecream")
#     return wrapper


# @deco   # decorator
# def ice_cream():
#     print("eating icecream")

# ice_cream()

# .............OR.............

# def deco(func):
#     def wrapper(*args, **kwargs):
#         print("added sprinklers")
#         func(*args, **kwargs)
#         print("finished icecream")
#     return wrapper


# @deco   # decorator
# def ice_cream(flavor):
#     print(f"eating {flavor} icecream")

# ice_cream("vanilla")





# Class Methods..........


# class Company:
#     company_name = "Tech Innovators"

#     @classmethod
#     def change_company_name(cls, new_name):
#         cls.company_name = new_name

# Company.change_company_name("Future solutions")
# print(Company.company_name)



# ..............Static Methods...............

# class MathOperations:
#     @staticmethod     #static method decorator
#     def add(a, b):
#         return a + b
    

# a = MathOperations()
# print(a.add(10,20))