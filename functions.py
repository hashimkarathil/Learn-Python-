# Functions..........................

# def greet(name):
#     print(f"Hello,{name}!")

# greet("Alice")


# Function Parameters and Arguments

# def add(a, b):
#     return a + b

# result =add(3,4)
# print(result)

# Positional Arguments:.........................

# def greet(name,age,place):
#     print(f"Hello {name},your age is {age},your place is {place}")

# greet("Hashim",25,"Malappuram")



# Keyword Arguments.................

# def greet(name,age,place):
#     print(f"Hello {name},your age is {age},your place is {place}")

# greet(name="Hashim",age=25,place="Malappuram")




# Default Arguments...............

# def greet(name,age,place="thirssur"):  #default parameter
#     print(f"Hello {name},your age is {age},your place is {place}")

# greet("Hashim",25,"Malappuram")
# greet("Vishnu",35)
# greet("Gowtham",20,"palakkad")




# Return Statement 

# def multiply(a,b):
#     return a*b

# result = multiply(4,5)
# print(result)


# Docstrings in Functions..........


# def add(a,b):
#     """This function adds two numbers"""
#     return a+b
# print(add.__doc__)



# 2. Lambda Functions in Python .............


# add = lambda a,b: a + b
# print(add(3,5))


# 3. Lambda Functions with map(), filter(), and reduce() Using Lambda with map() .........................................


# map()

# numbers = [1,2,3,4]
# squared = map(lambda x:x **2,numbers)
# print(list(squared))


# filter()

# numbers = [1,2,3,4]
# even_numbers = filter(lambda x:x % 2 == 0,numbers)
# print(list(even_numbers))


# numbers = [1,2,3,4,5]
# odd_numbers = filter(lambda x:x % 2 != 0,numbers)
# print(list(odd_numbers))


#  reduce() 
# from functools import reduce
# numbers = [1,2,3,4,5]
# sum_result = reduce(lambda x,y: x + y,numbers)

# print(sum_result)


# 4. Higher-Order Functions..............

# def  calculate(a,b,operation):
#     return operation(a,b)

# add=lambda x,y:x+y
# minus=lambda x,y:x-y

# print(calculate(10,20,add))
# print(calculate(10,20,minus))

#.........................................

# normal function lambda

# multi=lambda x,y:x*y
# print(multi(10,20))



# 5. Function Scope..............
# LEGB (Local, Enclosing, Global, Built-in).......

# x = 20   #global variable
# def outer():
#     # x=30     #enclosing variable
#     print(x)
#     def local():
#         x = 10   # local variable
#         print(x)
#     local()

# outer()

# print(x)


# 1. Arbitrary Arguments (*args) .........................

# example:

# def abc(*a):
#     print(a)
# abc(1,2,3,4,5,6)


# def sum_numbers(*args):
#     total=1
#     for number in args:
#         total += number
#     return total
# result= sum_numbers(1,2,3,4,5)
# print(result)




# 2. Keyword Arguments (**kwargs) ...............

# example

# def abc(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")

# abc(name="Hashim",age=24,place="Perinthalmanna")



# 3. Using *args and **kwargs Together 

# def display_info(*args, **kwargs):
#     print("Positional arguments:",args)
#     print("Positional arguments:",kwargs)

# display_info(1,2,3,name="Alice",age="25")


# order of arguments

# def display_info(param1, *args, **kwargs):
#     print("Positional arguments:",param1)
#     print("Positional arguments:",args)
#     print("Positional arguments:",kwargs)

# display_info(1,2,3,name="Alice",age="25")


# Recursion in Python......................................

# def factorial(n):
#     if n ==0 or n==1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))




# factorial ittration............

# def factorial(n):
#     total = 1
#     for i in range(1,n+1):
#         total*= i
#     return total
# print( factorial(5))



# 4. Tail Recursion..............

# def tail_factorial(n, accumulator=1):
#     if n == 0 or n == 1:
#         return accumulator
#     else:
#         return tail_factorial(n-1, accumulator*n)
    
# print(tail_factorial(5))


# 5. Common Examples of Recursion 
# a. Fibonacci Sequence:.....................


# def fibonscci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonscci(n-1)+ fibonscci(n-2)
    
# print(fibonscci(6))

# b. Sum of a List: .............

# def sum_list(lst):
#     if not lst:
#         return 0
#     else:
#         return lst[0]+ sum_list(lst[1:])
# print(sum_list([1,2,3,4,5]))