#.............Control and Conditional statements Tasks........

# 1. Check whether a number is positive, negative, or zero
# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# Output: Enter a number: 2                                                                                
# Positive    


# 2. Check if a number is even or odd
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# ouput: Enter a number: 3
# Odd


# 3. Given a number, check if it is greater than 100
# num = int(input("Enter a number: "))
# if num > 100:
#     print("Greater than 100")
# else:
#     print("Not greater than 100")

# Output : Enter a number: 203
# Greater than 100


# 4. Check whether a person is eligible to vote
# age = int(input("Enter age: "))
# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")

# Output : Enter age: 25
# Eligible to vote


# 5. Given two numbers, print the greater number
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b:
#     print("Greater number =", a)
# else:
#     print("Greater number =", b)

# Output : Enter first number: 34
# Enter second number: 33
# Greater number = 34


# 6. Given three numbers, print the largest number
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a >= b and a >= c:
#     print("largest=", a)
# elif b >= a and b >= c:
#     print("largest=", b)
# else:
#     print("largest=", c)

# Output : Enter first number: 3
# Enter second number: 4
# Enter third number: 5
# largest= 5


# 7. Check whether a year is a leap year
# year = int(input("Enter year: "))
# if (year % 4 == 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

# Output : Enter year: 2024
# Leap Year


# 8. Pass or Fail
# marks = int(input("Enter marks: "))
# if marks >= 40:
#     print("Pass")
# else:
#     print("Fail")

# Output : Enter marks: 41
# Pass


# 9. Print grades
# marks = int(input("Enter marks: "))
# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# elif marks >= 60:
#     print("Grade C")
# elif marks >= 45:
#     print("Grade D")
# else:
#     print("Fail")


# Output : Enter marks: 65
# Grade C


# 10. Check if a character is a vowel or consonant
# ch = input("Enter a character: ").lower()
# if ch in "aeiou":
#     print("Vowel")
# else:
#     print("Consonant")

# Output : Enter a character: apple
# Consonant


# 11. Print numbers from 1 to 10 but stop when number is 6
# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)

# Output : 1
# 2
# 3
# 4
# 5


# 12. Print numbers from 1 to 10 but skip number 5
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)


# Output : 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10


# 13. Use pass inside an if block
# num = 10
# if num > 5:
#     pass
# print("code continues")

# Output : code continues


# 14. Print all even numbers between 1 and 20
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

# Output :2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20


# 15. Find the sum of numbers from 1 to 10
# total = 0
# for i in range(1, 11):
#     total += i
# print("Sum =", total)


# Output : Sum = 55


# 16. Check whether a given number is a multiple of both 3 and 5
# num = int(input("Enter a number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print("Multiple of both 3 and 5")
# else:
#     print("Not a multiple of both 3 and 5")


# Output : Enter a number: 15
# Multiple of both 3 and 5


# 17. Print "Hello" 5 times using a loop
# for i in range(5):
#     print("Hello")

# Output : Hello
# Hello
# Hello
# Hello
# Hello


# 18. Given a list [1,2,3,4,5], print only numbers greater than 3
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num > 3:
#         print(num)


# Output : 4
# 5


# 19. Advanced Login System
# username = "admin"
# password = "1234"

# count = 0

# while count < 3:
#     usr = input("Enter username: ")
#     paswrd = input("Enter password: ")

#     if usr == username and paswrd == password:
#         print("Login Successful")
#         break
#     else:
#         count += 1
#         print("Wrong Username or Password")

# if count == 3:
#     print("Account Locked")


# output:
# Enter username: admin
# Enter password: 1234
# Login Successful


# 20. Enhanced Traffic Light Controller
# signal = input("Enter signal color or number: ").lower()

# if signal == "1" or signal == "red":
#     print("Stop and wait for 60 seconds")
# elif signal == "2" or signal == "yellow":
#     print("Ready and wait for 5 seconds")
# elif signal == "3" or signal == "green":
#     print("Go and drive safely")
# else:
#     print("Invalid signal")

# ouput: 
# Enter signal color or number: green
# Go and drive safely














# List Comprehension Tasks................................

# 1. Given a list of numbers, write a program to find the sum of all numbers, the sum of even numbers, and the sum of odd numbers using list comprehension.

# numbers = [1, 2, 3, 4, 5, 6]

# sum_all = sum([x for x in numbers])
# sum_even  = sum([x for x in numbers if x  % 2  == 0])
# sum_odd  = sum([x for x in  numbers if x %  2  != 0])

# print("Sum of all  numbers:" , sum_all)
# print("Sum of  even numbers:",  sum_even)
# print("Sum of odd  numbers:", sum_odd)

# output: 
# Sum of all numbers: 21
# Sum of even numbers: 12
# Sum of odd numbers: 9


# 2. Given a list of numbers, create a new list that contains only numbers greater than 10 and divisible by 3 using list comprehension.

# numbers = [5, 12, 15, 18, 20, 21, 25, 30]

# result = []

# for num in numbers:
#     if num > 10 and num % 3 == 0:
#         result.append(num)

# print(result)

# ouput: [12, 15, 18, 21, 30]



# 3. Given a list of numbers, create a new list containing only even numbers greater than 10 using list comprehension.

# numbers = [4, 8, 12, 15, 18, 22, 25, 30]

# result = []

# for num in numbers:
#     if num > 10 and num % 2 == 0:
#         result.append(num)

# print(result)

# ouput: [12, 18, 22, 30]



# 4. Given a list of strings, create a new list containing the length of each string using list comprehension.

# strings = ["apple", "banana", "cat", "elephant"]

# result = []

# for word in strings:
#     result.append(len(word))

# print(result)

# ouput: [5, 6, 3, 8]


# 5. Given a list of numbers, create a new list where even numbers are replaced with "even" and odd numbers are replaced with "odd".
# numbers = [1, 2, 3, 4, 5, 6]

# result = []

# for num in numbers:
#     if num % 2 == 0:
#         result.append("even")
#     else:
#         result.append("odd")

# print(result)

# ouput: ['odd', 'even', 'odd', 'even', 'odd', 'even']