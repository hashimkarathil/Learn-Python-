# 1. Creating a Dictionary

# Using curly braces
# my_dict = {"name":"john","age":"30","city":"New York"}
# print(my_dict)

# Using the dict() constructor
# another_dict = dict(naem="Alice",age=25,city="Los Angeles")
# print(another_dict)

# Empty Dictionary
# empty_dict ={}
# print(empty_dict)


# 2. Accessing Dictionary Items

# my_dict = {"name":"john","age":"30","salary":30000}
# print(my_dict["name"])


# Using get()

# print(my_dict.get("age"))
# print(my_dict.get("salary"))


# 3. Changing Dictionary Items

# my_dict = {"name":"john","age":"30"}
# my_dict["age"]=31
# print(my_dict)

# add new "key" and "value"
# my_dict["city"] = "New York"
# print(my_dict)

# 4. Adding Items to a Dictionary

# my_dict = {"name":"john","age":"30"}
# my_dict["city"] = "New York"
# print(my_dict)

# 5. Removing Items from a Dictionary

# pop(key)

# my_dict = {"name":"john","age":"30"}
# age = my_dict.pop("age")
# print(age)
# print(my_dict)


# popitem()

# my_dict = {"name":"john","age":"30"}
# last_item = my_dict.popitem()
# print(last_item)

#  del statement

# my_dict = {"name":"john","age":"30"}
# del my_dict["age"]
# print(my_dict)


# clear()
# my_dict = {"name":"john","age":"30"}
# my_dict.clear()
# print(my_dict)


# 6. Copying a Dictionary

# Using copy()

# original = {"name":"john","age":"30"}
# copy_dict =original.copy()
# print(copy_dict)

# Using dict() constructer
# original = {"name":"john","age":"30"}
# copy_dict = dict(original)
# print(copy_dict)

# 7. Nested Dictionaries

# nested_dict ={
#     "person1":{"name":"john","age":30},
#     "person2":{"name":"Alice","age":25},
# }

# print(nested_dict["person2"]["name"])


# 8. Dictionary Methods

# keys()

# my_dict = {"name":"john","age":30}
# print(my_dict.keys())

# values()
# my_dict = {"name":"john","age":30}
# print(my_dict.values())

# items()
# my_dict = {"name":"john","age":30}
# print(my_dict.items())

# update()
# my_dict = {"name":"john","age":30}
# my_dict.update({"name":"john","age":30,"city":"malappuram"})
# print(my_dict)


# fromkeys()
# keys = {"name":"john","age":30}
# new_dict = dict.fromkeys(keys, "Unknown")
# print(new_dict)


# setdefault(key, value)

# my_dict = {"name":"john","age":30}
# city = my_dict.setdefault("city","new york")
# print(city)
# print(my_dict)