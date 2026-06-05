# ..............Sets................


# 1. Creating

# Using curly braces
# my_set = {1,2,3,4}
# print(my_set)

# Using set() function
# another_set = set([5,6,7])
# print(another_set)

# Empty set

# empty_set = set()
# print(type(empty_set))

# 2.  Accessing Set Items

# my_set = {10,20,30,40}
# for item in my_set:
#     print(item)

# cehck element in a set
# my_set = {1,2,3,}
# print(2 in my_set) 
# print(5 in my_set) 

# 3. Adding Items to a Set

# Adding a single Item

# my_set = {1,2,3}
# my_set.add(4)
# print(my_set)

# Adding multiple items

# my_set = {1,2,3}
# my_set.update([4,5,6])
# print(my_set)

# 4. Removing Items from a Set

# remove()

# my_set={1,2,3,4}
# my_set.remove(2)
# print(my_set)

# discard()

# my_set = {1,2,3,4}
# my_set.discard(5)
# print(my_set)

# Pop()

# my_set = {1,2,3,4}
# removed_item = my_set.pop()
# print(removed_item)

# clear()
# my_set ={1,2,3}
# my_set.clear()
# print(my_set)

# 5. Joining Sets

# Union()

# set1 = {1,2,3}
# set2 = {3,4,5}
# result = set1.union(set2)
# print(result)

#or 

# set1 = {1,2,3}
# set2 = {3,4,5}
# result = set1 | set2
# print(result)

# update()

# set1 = {1,2,3}
# set2 = {3,4,5}
# set1.update(set2)
# print(set1)

#  Set Intersection (&)

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# result = set1 & set2
# print(result)

# Set Difference (-)

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# result = set1 - set2
# print(result)

#Set Symmetric Difference (^)

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# result = set1 ^ set2
# print(result)

# 6. Set Methods
# add
# remove
# discard
# pop
# clear
# copy
# union
# update
# intersection
# difference
# symmetric_difference


# issubset(set)
# set1 = {1,2}
# set2 = {1,2,3,4}
# print(set1.issubset(set2))


# # issuperset(set)
# set1 = {1,2}
# set2 = {1,2,3,4}
# print(set2.issuperset(set1))


# 7. 7. Frozen Sets
# my_frozenset = frozenset([1, 2, 3, 4])
# print(my_frozenset)