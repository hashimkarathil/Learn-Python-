# ..............File Handling...............


# Reading Files.....................

# 1. read() Method

# file = open("sample.txt", "r")
# content = file.read() 
# print(content) 
# file.close()

# 2. readline() Method

# file = open("sample.txt", "r")
# line1 = file.readline() 
# print(line1) 
# file.close() 

# 3. readlines() Method 

# file = open("sample.txt", "r")
# lines = file.readlines() 
# print(lines) 
# file.close() 


# Writing to Files......................

# 1. write()

# file = open("sample.txt","w")
# file.write("Hello, World!")
# file.close()

# 2. writelines() Method 

# file = open("sample.txt", "w") 
# lines = ["Hello\n", "Welcome to Python file handling\n"] 
# file.writelines(lines) 
# file.close()


# new txt file create through the directory

# file = open("D:/SOFTRONIICS/Python/Day1/sample2.txt", "w") 
# lines = ["Hello\n", "Welcome to Python file handling\n"] 
# file.writelines(lines) 
# file.close()


# Appending Data........................

# file = open("sample.txt", "a") 
# file.write("Appended text.\n") 
# lines = ["Hello\n", "Welcome to Python file handling\n"] 
# file.writelines(lines) 
# file.close() 

# Using with Statement.......

# with open("sample.txt","r") as file:
#     content = file.read()
#     print(content)


# File Positioning (Seek and Tell) ..............

# file=open("sample.txt","r")
# file.seek(5)
# print(file.read())
# file.close()

