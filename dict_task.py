# ...............Dictionary Task.............

# 1. Create a dictionary
# my_dict = {"name": "Nik", "age": 20}
# print(my_dict)

# ouput: {'name': 'Nik', 'age': 20}

# 2. Access the value of key "name"
# my_dict = {"name": "Nik", "age": 20}
# print(my_dict["name"])

# ouput: Nik

# 3. Add a new key "city"
# my_dict = {"name": "Nik", "age": 20}
# my_dict["city"] = "Delhi"
# print(my_dict)

# ouput: {'name': 'Nik', 'age': 20, 'city': 'Delhi'}

# 4. Update the value of "age" to 25
# my_dict = {"name": "Nik", "age": 20}
# my_dict["age"] = 25
# print(my_dict)

# ouput: {'name': 'Nik', 'age': 25}

# # 5. Delete the key "age"
# my_dict = {"name": "Nik", "age": 20}
# del my_dict["age"]
# print(my_dict)

# ouput: {'name': 'Nik'}

# 6. Check if the key "email" exists
# my_dict = {"name": "Nik", "age": 20}
# print("email" in my_dict)

# ouput: False

# 7. Get all keys
# my_dict = {"name": "Nik", "age": 20}
# print(my_dict.keys())

# ouput: dict_keys(['name', 'age'])

# 8. Get all values
# my_dict = {"name": "Nik", "age": 20}
# print(my_dict.values())

# ouput: dict_values(['Nik', 20])

# 9. Convert dictionary into a list of (key, value) pairs
# my_dict = {"a": 1, "b": 2}
# print(list(my_dict.items()))

# ouput: [('a', 1), ('b', 2)]

# 10. Create a dictionary from two lists
# keys = ["name", "age"]
# values = ["Nik", 20]
# my_dict = dict(zip(keys, values))
# print(my_dict)

# ouput: {'name': 'Nik', 'age': 20}

# 11. Count how many keys are in the dictionary
# my_dict = {"a": 1, "b": 2, "c": 3}
# print(len(my_dict))

# ouput: 3

# 12. Merge two dictionaries
# my_dict = {"a": 1}
# dict2 = {"b": 2}
# merged_dict = {**my_dict, **dict2}
# print(merged_dict)

# ouput: {'a': 1, 'b': 2}

# 13. Clear all elements
# my_dict = {"a": 1, "b": 2}
# my_dict.clear()
# print(my_dict)

# ouput: {}

# 14. Copy the dictionary
# my_dict = {"x": 10, "y": 20}
# copy_dict = my_dict.copy()
# print(copy_dict)

# ouput: {'x': 10, 'y': 20}

# 15. Get the value of key "salary" safely
# my_dict = {"name": "Nik", "age": 20,"salary":30000}
# print(my_dict.get("salary"))

# ouput: 30000

# 16. Remove the last inserted item
# my_dict = {"a": 1, "b": 2, "c": 3}
# my_dict.popitem()
# print(my_dict)

# ouput: {'a': 1, 'b': 2}

# 17. Access only the "science" marks
# my_dict = {
#     "name": "Rahul",
#     "marks": {"math": 90, "science": 85}
# }
# print(my_dict["marks"]["science"])

# ouput: 85

# 18. Update "math" marks to 95
# my_dict = {
#     "name": "Rahul",
#     "marks": {"math": 90, "science": 85}
# }
# my_dict["marks"]["math"] = 95
# print(my_dict)

# ouput: {'name': 'Rahul', 'marks': {'math': 95, 'science': 85}}

# 19. Add a new subject "english": 88
# my_dict = {
#     "name": "Rahul",
#     "marks": {"math": 90, "science": 85}
# }
# my_dict["marks"]["english"] = 88
# print(my_dict)

# ouput: {'name': 'Rahul', 'marks': {'math': 90, 'science': 85, 'english': 88}}

# 20. Delete the subject "science"
# my_dict = {
#     "name": "Rahul",
#     "marks": {"math": 90, "science": 85}
# }
# del my_dict["marks"]["science"]
# print(my_dict)

# ouput: {'name': 'Rahul', 'marks': {'math': 90}}