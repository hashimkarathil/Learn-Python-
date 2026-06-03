# print("hello world")

# if 5 > 2:
#     print("5 is greater than 2")
#....................................................

# 1. Numeric Types 

# age = 15
# print(age)
# 1.1 float
# float = 15.1
# print(float)

# 2. str
# name = "hashim"
# print(name)

# 3. boolean
# is_active = True
# print(is_active)

# 4. List type
# fruits = ["apple","banana","orange"]
# print(fruits)
# print(fruits[0])

# 5. Tuple type
# fruits = ("apple","banana","orange","grapes")

# 6. Dictionary Type
# user = {"name":"Hashim","age":25}
# print(user["name"])

# 7 . Set Type
# fruits = {"apple","orange","grape"}

# .................... Variable Assignment and Operations..............

#Variable Assignment
# x = 10
# y = 3.5
# name = "john"
# is_student = True

# 1. Arithematic operater
# a=5
# b=4
# print(a+b)
# print(a-b)
# print(a%b)
# print(a/b)

# 2. Assignment opeartor
# a=40
# b=20
# # print(a**b)
# # print(a)
# # print(a+5)
# print(a==b)

# 3. logical opeartor
# a = 5
# b = 10
# print(a>b and b>a)
# print(a>b or b>a)
# print(not  b<a)

# 4. comparison operator
# a = 15
# print(a == b)
# print(a != b)
# print(a<b)


# 5. identity operator

#compare the memory location of two objects
# b = 5
# print(a is not b)

# 6. Membership operator

#membership check for membership in sequence
# a = "Hello world"
# print("world" in a)

#.......................Strings Overview ....................

#........String Slicing
#Basic Slicing:
# s = "Hello, world"
# print(s[0:5])

#Negative Indices
# print(s)

#................Python Strings.................

# 3. String Concatenation........

#  Using + operator
# s1 = "Hello"
# s2 = "World"
# result = s1 + "," + s2 + "!"
# print(result)

# using join() method
# words = ["python","is","awesome"]
# sentence = " ".join(words)
# print(sentence)


# 4. Format Strings..........

#  Using % operator
# name ="Alice"
# age = 25
# formatted_string = "My name is %s , and %d year old. "%(name, age)
# print(formatted_string)

# Using format() method
# name = "Bob"
# age = 30
# formatted_string = "My name is {} , and {} year old. ".format(name, age)

# Using F string
# formatted_string = f"My name is {name},and my age is {age}"


# 5. Escape Characters.....................

# print("Hello \nWorld")
# print("Hello \tWorld")
# print("Hello \'World")
# print("Hello \"nWorld")
# print("Hello \\nWorld")
# Using quotes within a string
# print('He said, "Python is amazing!"')

# 6. String Methods
# s = "Hello, World"
# print(len(s))
# strip()
# print(s.strip())
#split()
# s = "Hello, World!"
# print(s.split(","))

#find()
# s = "Hello, World!"
# print(s.find("World"))

#Count ()
# s = "Hello,Hello, World!"
# print(s.count("Hello"))

# Stratwith and endwith

# s = "Hello, World!"
# print(s.startswith("Hello")) 
# print(s.endswith("World!")) 


#upper() and lower()
# s = "Hello, World!"
# print(s.upper())
# print(s.lower())

#replace
# s = "Hello, World!"
# print(s.replace("World","Python"))
