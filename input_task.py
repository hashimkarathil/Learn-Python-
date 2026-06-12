
x = int(input("enter a number"))
y = int(input("enter a second number"))
z = input("select opreator")

if z == "+":
    print(x+y)
elif z == "-":
    print(x-y)
elif z == "*":
    print(x*y)
elif z == "/":
    print("you can divide by 0" if y == 0 else x/y) 
else:
    print("invalid")

    