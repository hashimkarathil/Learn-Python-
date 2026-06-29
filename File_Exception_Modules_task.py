# .........File Exception Modules Tasks.................


# FILE HANDLING
# 1. Write a program to create a file named data.txt and write the text "Hello File Handling" into it.

# with open('data.txt','w') as e:
#     e.write('Hello File Handling')
# print('File created')

# ouput: File created


# 2. Write a program to read the contents of a file data.txt and display it on the screen.

# with open('data.txt','r') as e:
#     print(e.read())

# output: Hello File Handling


# 3. Write a program to append the text "Python is awesome" to an existing file.

# with open('data.txt','a') as e:
#     e.write('\nPython is awesome')
# print('Appended')

# output: Appended


# 4. Write a program to count the number of lines present in a file.

# with open('data.txt') as e:
#     print(len(e.readlines()))

# output: 2


# 5. Write a program to count the number of words in a file.

# with open('data.txt') as f:
#     print(len(f.read().split()))


# ouput: 6


# 6. Write a program to copy the contents of one file into another file.

# open('copy.txt','w').write(open('data.txt').read())
# print('Copied')


# output: Copied


# 7. Write a program to read a file and print only the lines that contain the word "Python" .

# with open('data.txt') as e:
#     for i in e:
#         if 'Python' in i:
#             print(i.strip())

# ouput: Python is awesome


# 8. Write a program that reads numbers from a file and calculates their sum.

# s=0
# with open('num.txt') as e:
#     for i in e:
#         s+=int(i)
# print(s)

# output: 60




# ERROR HANDLING (EXCEPTION HANDLING)...............


# 9. Write a program to handle a ValueError when the user enters invalid input (for example, entering letters instead of a number).

# try:
#     n=int(input())
# except ValueError:
#     print('Invalid input')


# output: s
# Invalid input 


# 10. Write a program to handle invalid input (user enters a string instead of a number).

# try:
#     x=int(input())
#     print(x)
# except:
#     print('Error')


# output: q
# Error


# 11. Write a program that handles file not found error while opening a file.

# try:
#     open('samples.txt')
# except FileNotFoundError:
#     print('File not found')

# output: File not found


# 12. Write a program using try , except , and else blocks.

# try:
#     x=10/2
# except:
#     print('Error')
# else:
#     print(x)

# output: 5.0



# 13. Write a program using try , except , and finally to ensure a message "Program ended" is always printed


# try:
#     print(10/2)
# except:
#     print('Error')
# finally:
#     print('Program ended')

# output: 5.0
# Program ended


# 14. Write a program that catches multiple exceptions using multiple except blocks.

# try:
#     x=int(input())
#     print(10/x)
# except ValueError:
#     print('Value Error')
# except ZeroDivisionError:
#     print('Divide by zero')


# output : 0
# Divide by zero


# 15. Write a program that raises a custom error when the user enters a negative number.

# n=int(input())
# if n<0:
#     raise ValueError('Negative number')


# output: ValueError: Negative number





# MODULES & LIBRARIES (BUILT-IN + USERDEFINED)......................

# 16. Write a program that uses the math module to find the square root of a number.

# import math
# print(math.sqrt(25))


# output: 5.0


# 17. Write a program that uses the math module to calculate power of a number.

# import math
# print(math.pow(2,3))

# output: 8.0


# 18. Write a program that uses the math module to find the factorial of a number

# import math
# print(math.factorial(5))

# output: 120


# 19. Create a user-defined module named calculator.py that contains functions
# for addition, subtraction, multiplication, and division.
# Import and use this module in another Python file.


# file name  "File_Exception_Modules_task.py"
# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# def div(a,b):
#     return a/b

# file name "main.py"
# import File_Exception_Modules_task

# print(File_Exception_Modules_task.add(2,3))
# print(File_Exception_Modules_task.sub(5,2))
# print(File_Exception_Modules_task.mul(4,3))
# print(File_Exception_Modules_task.div(10,2))

# output:
# 5
# 3
# 12
# 5.0


# 20. Create a user-defined module that contains a function to check whether a number
# is even or odd, and use it in another program.

# file name "File_Exception_Modules_task.py"

# def check(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
    

# file name "main.py"
# import File_Exception_Modules_task

# n = int(input("Enter a number: "))

# print(File_Exception_Modules_task.check(n))



# ouput: Enter a number: 2
# Even


# 21. Create a user-defined module with a function that returns the area of a circle,
# and import it in another file.


# file name "File_Exception_Modules_task.py"

# def area(r):
#     return 3.14 * r * r


# file name: "main.py"

# import File_Exception_Modules_task

# r = float(input("Enter the radius: "))

# print("Area of Circle =", File_Exception_Modules_task.area(r))


# output: Enter the radius: 5
# Area of Circle = 78.5
