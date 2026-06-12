# 1. Conditional Statements (if, elif, else)

# if Statement

# x = 10
# if x > 5:
#     print("x is greater than 5")


# if-else Statement

# x = 3
# if x > 5:
#     print("x is greater than 5")
# else:
#     print("x is less than or equal to 5")


# if-elif-else Statement

# x = 7

# if x > 10:
#     print("x is greater than 10")
# elif x > 5:
#     print("x is greater than 5 but less than or equal to 10")
# else:
#     print("x is less than or equal to 5")


# 2. Nested if Statements................


# x = 10
# y = 5
# if x > 5:
#     if y  < 10:
#         print("x is greater than 5 and y is less than 10")



# 3. Python's if with and, or, not (Logical Operators).........



# And

# x = 10
# y = 5
# if x > 5 and y < 10:
#     print("both contions are true")


# OR

# x = 10
# y = 5
# if x > 5 or y > 10:
#     print("At least one conditin is true")


# NOT

# x = 10
# y = 5
# if not x < 5:
#     print("x is not less than is true")



# 4. Conditional Expressions (Ternary Operator)...........

# x = 5
# result = "greater than 10" if x > 10 else "10 or less"
# print(result)





# input form user..........................

# x = int(input("enter a number: "))      
                                        
# if x > 5:
#     print("greater than 5")
# elif x == 5:
#     print("the entered number 5")
# else:
#     print("less than 5")

#.........................................


# x = 10
# y = 5

# if x > 5 :
#     if y > 10:
#         print("x is greater than 5 and y is less than 10")
#     else:
#         print("x is greater than 5 and y is greater than 10")
# else:
#     print("x is less than 5")
    

# 5. Control Flow Statements

# 5.1 The pass Statement 

# x = 5
# if x > 3:
#     pass

# 5.2 The continue Statement 

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)


# 5.3 The break Statement 

# for i in range(5):
#     if i == 3:
#         break
#     print(i)

# 6. Loops in python 

# 6.1 FOR Loop

# fruits =["apple","banana","cherry"]
# for fruit in fruits:
#     print(fruit)

# 6.2 while Loop

# x = 0
# while x < 5:
#     print(x)
#     x +=1



# 7. else with Loops 


# with for loop: 

# for i in range (5):
#     print(i)
# else:
#     print("Loop completed")


# with while loop: 

# x = 0
# while x <5:
#     print(x)
#     x += 1
# else:
#     print("Loop completed")

# 8. Nested Loops

# for i in range(3):
#     for j in range(2):
#         print(f"i = {i}, j = {j}")


# 9. Infinite  Loop

# while True:
#     print("This is an infinite loop")