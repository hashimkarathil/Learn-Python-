# ...............Python-Error Handling.........

# 1. Errors in Python

# Error............
# print("hello"

# Error correct ............
# print("hello")


# 2. Common Python Exceptions

# 2.1. ZeroDivisionError.....

# Error............
# a=10
# b=0
# print(a/b)

# Error correct ............
# a=10
# b=0
# try:
#     print(a/b)
# except Exception as e:
#     print(e)

# 2.2. TypeError......

# a = 10
# b="5"
# print(a+b)

# 2.3. Value error.....

# num = int("abc")
# print(num) ................. error

# num = int(2)
# print(num)  .............. correct



# 2.4. Index error..........

# numbers = [10, 20, 30]
# print(numbers[5]) # error
# print(numbers[1]) # correct



# 2.5. KeyError............


# student = {"name": "John", "age": 20}

# # print(student["grade"]) # error
# print(student["name"]) # correct 


# 2.6. File not found error.............


# file = open("sampless.txt", "r")  # no define "file name"
# content = file.read() 
# print(content) 
# file.close()


# 3. try-except...........

# try:
#     x= 10/0
# except ZeroDivisionError:
#     print("You can't divide by zero")

# 4. Using else and finally in Exception Handling..

# try:
#     num = int(input("enter a number: "))
#     result = 10/ num
# except ZeroDivisionError:
#     print("Division by zero is not allowed!")
# else:
#     print(f"The result is {result}")
# finally:
#     print("this will always be printed")

# 5. Raising Exceptions......

# x = -5
# if x <0:
#     raise ValueError("negative numbers are not allowed")


# 6. Custom Exceptions.........

class negativeNumberError(Exception):
    pass

def check_number(num):
    if num < 0:
        raise negativeNumberError("negative numbers are not allowed!")
    
try:
    check_number(-10)
except  negativeNumberError as e:
    print(e)
