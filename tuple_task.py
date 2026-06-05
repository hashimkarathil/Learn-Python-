# ............Tuple Task.........

# 1. Create a tuple (1,2,3,4) and access the element 3 using indexing.

# my_tuple = (1,2,3,4)
# print(my_tuple[3])
# ouput: 4

# 2. Convert the tuple (10,20,30) into a list
# my_tuple = (10,20,30)
# my_list = list(my_tuple)
# print(my_list)

# ouput: [10, 20, 30]

# 3. Convert the list [1,2,3] into a tuple.
# my_list = [1,2,3]
# my_tuple = tuple(my_list)
# print(my_tuple)

# ouput: (1, 2, 3)

# 4. From the tuple ("a","b","c","d") , extract ("b","c") using slicing.

# my_tuple = ("a","b","c","d")
# print(my_tuple[1:3])

# ouput: ('b', 'c')

# 5. Check if "x" exists inside the tuple ("x","y","z") .

# my_tuple=("x","y","z")
# print(my_tuple.index("x"))

# ouput: 0


# 6. Given (5,3,9,1) , find the maximum value using a tuple function.

# my_tuple = (5,3,9,1)
# maximum = max(my_tuple)
# print(maximum)

# ouput: 9

# 7. Given (1,2,3) , create a new tuple (1,2,3,1,2,3) using tuple operations only.
# my_tuple = (1,2,3)
# another_tuple = (1,2,3)
# new_tuple = my_tuple + another_tuple
# print(new_tuple)

# output : (1, 2, 3, 1, 2, 3)

# 8. Count how many times 2 appears in (1,2,2,3,2) using a tuple method.

# my_tuple= (1,2,2,3,2)
# print(my_tuple.count(2))

# output: 3

# 9. Find the index of "cat" in ("dog","cat","mouse")
# my_tuple = ("dog", "cat", "mouse")
# print(my_tuple.index("cat"))

# output: 1

# 10. Reverse (1,2, 3,4,5) using slicing
# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[::-1])

# output: (5, 4, 3, 2, 1)


# 11. Combine (1,2) and (3,4) into (1,2,3,4) using tuple operations
# my_tuple = (1, 2)
# print(my_tuple + (3, 4))

# output: (1, 2, 3, 4)

# 12. Convert "hello" into a tuple of characters
# my_tuple = tuple("hello")
# print(my_tuple)

# output: ('h', 'e', 'l', 'l', 'o')


# 13. Convert (1,2,3,4) into the list [1,4] by extracting only first & last elements
# my_tuple = (1, 2, 3, 4)
# result = [my_tuple[0], my_tuple[-1]]
# print(result)

# output: [1, 4]


# 14. Given a tuple (10,20,30,40), replace the value 30 with 99
# my_tuple = (10, 20, 30, 40)
# temp = list(my_tuple)
# temp[2] = 99
# my_tuple = tuple(temp)
# print(my_tuple)

# output: (10, 20, 99, 40)


# 15. Using unpacking, extract a=1, b=2, c=3 from (1,2,3)
# my_tuple = (1, 2, 3)
# a, b, c = my_tuple
# print(a, b, c)

# output: 1 2 3

# 16. Create a nested tuple: turn (1,2,3) into ((1,2,3),)
# my_tuple = (1, 2, 3)
# my_tuple = (my_tuple,)
# print(my_tuple)

# output: ((1, 2, 3),)


# 17. Merge ("a","b") with ["c","d"] to get ("a","b","c","d")
# my_tuple = ("a", "b")
# my_list = ["c", "d"]
# result = my_tuple + tuple(my_list)
# print(result)

# output: ('a', 'b', 'c', 'd')

# 18. Check if tuple (1,2,3) is equal to its reverse
# my_tuple = (1, 2, 3)
# print(my_tuple == my_tuple[::-1])

# output: False


# 19. Convert a tuple of lists ([1,2],[3,4]) into a single flat list [1,2,3,4]
# my_tuple = ([1, 2], [3, 4])
# result = my_tuple[0] + my_tuple[1]
# print(result)

# output: [1, 2, 3, 4]

# 20. Given (1, [2,3], 4), add 5 inside the inner list
# my_tuple = (1, [2, 3], 4)
# my_tuple[1].append(5)
# print(my_tuple)

# output: (1, [2, 3, 5], 4)