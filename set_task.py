# 1. Create a set with values {1, 2, 3, 4}
# my_set = {1, 2, 3, 4}
# print(my_set)

# output: {1, 2, 3, 4}


# 2. Add the value 5 to the set {1, 2, 3, 4}
# my_set = {1, 2, 3, 4}
# my_set.add(5)
# print(my_set)

# output: {1, 2, 3, 4, 5}

# 3. Remove the value 3 from the set {1, 2, 3, 4}
# my_set = {1, 2, 3, 4}
# my_set.remove(3)
# print(my_set)

# output: {1, 2, 4}

# 4. Check if 2 exists in the set {1, 2, 3, 4}
# my_set = {1, 2, 3, 4}
# print(2 in my_set)

# output: True

# 5. Convert the list [1, 2, 2, 3, 4, 4] into a set
# my_list = [1, 2, 2, 3, 4, 4]
# my_set = set(my_list)
# print(my_set)

# output: {1, 2, 3, 4}


# 6. Convert the tuple (10, 20, 30) into a set
# my_tuple = (10, 20, 30)
# my_set = set(my_tuple)
# print(my_set)

# output: {10, 20, 30}

# # 7. Find the union of sets {1, 2, 3} and {3, 4, 5}
# my_set = {1, 2, 3}
# print(my_set.union({3, 4, 5}))

# output: {1, 2, 3, 4, 5}


# 8. Find the intersection of sets {1, 2, 3} and {3, 4, 5}
# my_set = {1, 2, 3}
# print(my_set.intersection({3, 4, 5}))

# output: {3}

# 9. Find the difference between sets {1, 2, 3, 4} and {3, 4}
# my_set = {1, 2, 3, 4}
# print(my_set.difference({3, 4}))

# output: {1, 2}


# 10. Create a copy of the set {5, 6, 7}
# my_set = {5, 6, 7}
# new_set = my_set.copy()
# print(new_set)

# output: {5, 6, 7}


# 11. Remove all elements from the set {1, 2, 3}
# my_set = {1, 2, 3}
# my_set.clear()
# print(my_set)

# output: set()


# 12. Check whether {1, 2} is a subset of {1, 2, 3}
# my_set = {1, 2}
# print(my_set.issubset({1, 2, 3}))

# output: True

# 13. Check whether {1, 2, 3} is a superset of {1, 2}
# my_set = {1, 2, 3}
# print(my_set.issuperset({1, 2}))

# output: True

# 14. Find the symmetric difference between {1, 2, 3} and {3, 4, 5}
# my_set = {1, 2, 3}
# print(my_set.symmetric_difference({3, 4, 5}))

# output: {1, 2, 4, 5}


# 15. Add multiple elements {8, 9, 10} into {1, 2, 3}
# my_set = {1, 2, 3}
# my_set.update({8, 9, 10})
# print(my_set)

# output: {1, 2, 3, 8, 9, 10}

# 16. Remove a random element from the set {1, 2, 3}
# my_set = {1, 2, 3}
# removed = my_set.pop()
# print("Removed:", removed)
# print(my_set)

# output: Removed: 1      {2, 3}


# 17. Check if two sets {1, 2, 3} and {3, 2, 1} are equal
# my_set = {1, 2, 3}
# print(my_set == {3, 2, 1})

# output: True

# 18. Extract only unique values from [1, 2, 2, 3, 4, 4, 5]
# my_list = [1, 2, 2, 3, 4, 4, 5]
# my_set = set(my_list)
# print(my_set)

# output: {1, 2, 3, 4, 5}

# 19. Convert the set {1, 2, 3} into a list
# my_set = {1, 2, 3}
# my_list = list(my_set)
# print(my_list)

# output: [1, 2, 3]

# 20. From {1, 2, 3, 4, 5}, remove {2, 4}
# my_set = {1, 2, 3, 4, 5}
# my_set.difference_update({2, 4})
# print(my_set)

# output: {1, 3, 5}
