fileName = input("enter the file name: ")

try:
    file = open(fileName,"r")
    print("file found")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("file not found")