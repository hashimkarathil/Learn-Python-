my_list = [1,2,3,4,5,6]


# 1. Finds the largest element in an array.
largest = max(my_list)
print(largest)

# 2. Finds the smallest element in an array.
largest = min(my_list)
print(largest)

# 3. Calculates the sum of all elements in the array
total = sum(my_list)
print(total)

# 4. Prints only the even numbers from the array.
even_number = filter(lambda x: x%2 == 0, my_list)
print(list(even_number))

# 5. Prints only the odd numbers from the array
odd_number = filter(lambda x: x%2 != 0, my_list)
print(list(odd_number))

# 6.  Counts the number of odd and even numbers in the array.
even = [x for x in my_list if x %2 == 0]
even_count = len(even)
print(even_count)


odd = [x for x in my_list if x %2 != 0]
odd_count = len(odd)
print(odd_count)

# 7. Calculates the sum of odd numbers in the array.
odd_sum = sum(odd)
print(odd_sum)

# Calculates the sum of even numbers in the array.
even_sum = sum(even)
print(even_sum)

#...............................................


# 2). number pyramid.....>


n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    
    for j in range(1, i + 1):
        print(j, end=" ")
        
    print() 