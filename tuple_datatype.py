#Tuple

# 1. Creating Tuple
# my_tuple = (1,2,3,'pyhton',4.5)
# print(my_tuple)

#single Item Tuple
# single_tuple = (5,)
# print(type(single_tuple))


# 2. Accessing Tuple Items

# my_tuple = ('apple','banana','cherry')
# print(my_tuple[1])
# print(my_tuple[-1])

# Slicing Tuples

# my_tuple = (10,20,30,40,50)
# print(my_tuple[1:4])

# 3. Updateing a Tuple

# Reassigning a Tuple:

# my_tuple = (1,2,3)
# my_tuple=(4,5,6)
# print(my_tuple)

# Convert Tuple to List
# my_tuple =('apple','banana','cherry')
# temp_list = list(my_tuple)
# temp_list[1] = 'orange'
# my_tuple=tuple(temp_list)
# print(my_tuple)


# 4. Unpacking Tuples
# my_tuple = ('apple','banana','cherry')
# (fruit1,fruit2,fruit3) = my_tuple
# print(fruit1)
# print(fruit2)
# print(fruit3)

# Using *(asterisk)
# my_tuple = (1,2,3,4,5)
# (fisrt,*middle,last) = my_tuple
# print(fisrt)
# print(middle)
# print(last)

# 5. Joining Tuples
# tuple1 =(1,2,3)
# tuple2=(4,5,6)
# joined_tuple = tuple1 + tuple2
# print(joined_tuple)

# 6. Tuple Methods
 
# count()
# my_tuple=(1,2,3,2,2,4)
# print(my_tuple.count(2))


# index()
# my_tuple = ('apple','banana','cherry')
# print(my_tuple.index('banana'))


# 7. Tuples vs Lists

#  Mutability: Lists are mutable, whereas tuples are immutable.


# 8. Deleting a Tuple

# my_tuple = ('apple','banana','cherry')
# del my_tuple
# print(my_tuple)

