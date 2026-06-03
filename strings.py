
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

