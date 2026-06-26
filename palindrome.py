num = input("enter a element: ").lower()

if num == num[::-1]:
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")