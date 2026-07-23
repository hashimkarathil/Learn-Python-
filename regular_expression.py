import  re


# 1. re.search()....

# text = "hello world"
# print(re.search(r"world", text))



# 2. re,match()....

# text = "hello world"
# print(re.match(r"hello", text))
# print(re.match(r"world", text))



# 3. re.findall()....

# text = "i have 2 apples and 3 bananas"
# print(re.findall(r"\d+", text))

# text = "the price is 45 dollars, 30 cents , and 50 rupees"
# print(re.findall(r"\d+", text))


# 4. re.finditer()....

# text = " i have 2 aoples and 3 bananas"
# for match in re.finditer(r"\d+", text):
#     print(match.group(), "at", match.start())



# 5. re.sub()....

# text = "hello 123, welcome 456!"
# print(re.sub(r"\d+", "number", text)) 


# 6. re.split()....

# text = "apple,orange;banana,grape"
# print(re.split(r"[,;]", text))




# Grouping & Capturing..............

# text = "john:34, jane:56, bob:78"
# print(re.findall(r"(\w+):(\d+)", text)) 




# Compiling Regex....................


# pattern = re.compile(r"\d+")
# text = "123 apples and 456 oranges"
# print(pattern.findall(text))


# ........Regex Flags........


# 1. re.IGNORECASE (or re.I )......

# text = "HELLO world"
# print(re.search(r"hello", text, re.IGNORECASE)) 


# 2. re.MULTILINE (or re.M )

text = """first line
second line
third line"""

print(re.findall(r"^s\w+", text, re.MULTILINE)) 

print(re.findall(r"\w+e$", text, re.MULTILINE)) 
