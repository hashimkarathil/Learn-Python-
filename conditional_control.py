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


x = 10
y = 5

if x > 5 :
    if y > 10:
        print("x is greater than 5 and y is less than 10")
    else:
        print("x is greater than 5 and y is greater than 10")
else:
    print("x is less than 5")
    