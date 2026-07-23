class Book:
    def __init__(self,title, author,copies):
        self.title = title
        self.author = author
        self.copies = copies

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Copies:", self.copies)

books =[]

title = input("Enter book title: ")
author = input("Enter author: ")
copies= input("Enter copies: ")
books.append(Book(title,author,copies))

title = input("Enter book title: ")
author = input("Enter author: ")
copies= input("Enter copies: ")
books.append(Book(title,author,copies))

title = input("Enter book title: ")
author = input("Enter author: ")
copies= input("Enter copies: ")
books.append(Book(title,author,copies))

search = input("Enter book title to search: ")

for book in books:
    if book.title == search:
        book.display_info()
        break
    else:
        print("book not available")
