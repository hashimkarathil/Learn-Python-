# 1. Check if a number is even or odd
# def check_even_odd(n):
#     return "Even" if n % 2 == 0 else "Odd"

# print(check_even_odd(10))

# ouput: Even


# 2. Return the largest of three numbers
# def find_largest(a, b, c):
#     return max(a, b, c)

# print(find_largest(5, 12, 8))

# output : 12


# 3. Return the sum of all elements in a list
# def sum_list(numbers):
#     return sum(numbers)

# print(sum_list([1, 2, 3, 4]))

# output: 10


# 4. Return a new list containing only even numbers
# def filter_even(numbers):
#     return [x for x in numbers if x % 2 == 0]

# print(filter_even([1, 2, 3, 4, 5, 6]))

# output: [2, 4, 6]

# 5. Return the length of a string
# def string_length(s):
#     return len(s)


# print(string_length('Hello World'))

# output: 11


# 6. Convert a string to uppercase
# def uppercase(s):
#     return s.upper()

# print(uppercase('hello'))

# output: HELLO


# 7. Check if a number is positive, negative, or zero
# def check_number(n):
#     if n > 0: return "Positive"
#     elif n < 0: return "Negative"
#     return "Zero"

# print(check_number(-5))

# output: Negative


# 8. Check if a number is a multiple of both 3 and 5
# def multiple(n):
#     return n % 3 == 0 and n % 5 == 0

# print(multiple(15))

# output: True


# 9. Return the maximum value in a list
# def find_max(numbers):
#     return max(numbers)

# print(find_max([10, 50, 20]))

# output: 50


# 10. Return the grade based on marks
# def grade(marks):
#     if marks >= 90: return "A"
#     elif marks >= 75: return "B"
#     elif marks >= 60: return "C"
#     return "Fail"

# print(grade(82))


# output: B


# 11. Return the price after a 10% discount
# def apply_discount(price):
#     return price * 0.90

# print(apply_discount(100))

# output: 90.0


# 12. Return the count of even and odd numbers in a list
# def count_even_odd(numbers):
#     even_count = sum(1 for x in numbers if x % 2 == 0)
#     odd_count = len(numbers) - even_count
#     return {"Even": even_count, "Odd": odd_count}

# print(count_even_odd([1, 2, 3, 4, 5]))

# output: {'Even': 2, 'Odd': 3}


# 13. Convert Celsius to Fahrenheit
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# print(celsius_to_fahrenheit(25))

# output: 77.0