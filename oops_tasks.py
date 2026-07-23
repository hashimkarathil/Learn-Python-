# Employee Bonus System...........

# class Employee:
#     def __init__(self, name, position,salary):
#         self.name = name
#         self.position = position
#         self.salary = salary

#     def apply_bonus(self, percentage):
#         self.salary = self.salary + (self.salary * percentage / 100)
    
#     def display_info(self):
#         print("Name:", self.name)
#         print("Position:", self.position)
#         print("Salary:", self.salary)

# name = input("Enter name: ")
# position = input("Enter position: ")
# salary = float(input("Enter salary: "))
# emp1 = Employee(name, position, salary)

# name = input("Enter name: ")
# position = input("Enter position: ")
# salary = float(input("Enter salary: "))
# emp2 = Employee(name, position, salary)

# bonus = float(input("Enter bonus % for employee1: "))
# emp1.apply_bonus(bonus)

# bonus = float(input("Enter bonus % for employee2: "))   
# emp2.apply_bonus(bonus)

# print("\nEmployee details")
# emp1.display_info()
# emp2.display_info()


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def apply_bonus(self, percentage):
        self.salary = self.salary + (self.salary * percentage / 100)

    def display_info(self):
        print("Name:", self.name,
              "| Position:", self.position,
              "| Salary:", self.salary)


employees = []

for i in range(2):
    print("\nEnter details of Employee", i + 1)

    name = input("Enter name: ")
    position = input("Enter position: ")
    salary = float(input("Enter salary: "))

    emp = Employee(name, position, salary)

    bonus = float(input("Enter bonus %: "))
    emp.apply_bonus(bonus)

    employees.append(emp)

print("\nUpdated Employee Details")


for emp in employees:
    emp.display_info()

# Enter details of Employee 2
# Enter name: alice
# Enter position: sales
# Enter salary: 30000
# Enter bonus %: 10

# Updated Employee Details
# Name: hashim | Position: manager | Salary: 55000.0
# Name: alice | Position: sales | Salary: 33000.0

# Shopping Cart Simulation....................

# class Cart:
#     def __init__(self):
#         self.products = []

#     def add_product(self, price):
#         self.products.append(price)

#     def total_price(self):
#         return sum(self.products)
    
# cart = Cart()

# for i in range(3):
#     name = input("Enter product name: ")
#     price = float(input("Enter product price: "))
#     cart.add_product(price)

# print("Total price: Rs", cart.total_price())





# Movie Ticket Booking....................


# class Movie:
#     def __init__(self, title, seats):
#         self.title = title
#         self.seats = seats
    
#     def book_ticket(self, n):
#         if n <= self.seats:
#             self.seats = self.seats - n
#             print(n,"tickets booked successfully.")
#         else:
#             print("Not enough seats ")

# tile = input("Enter movie title: ")
# seats = int(input("Enter available seats: "))

# movie = Movie(tile, seats)

# book =int(input("enter seats to book: "))
# movie.book_ticket(book)

# book =int(input("enter seats to book: "))
# movie.book_ticket(book)




# Loan Eligibility....................


# class Customer:
#     def __init__(self,name,income,credit_score):
#         self.name = name
#         self.income = income
#         self.credit_score = credit_score
    
#     def check_eligibility(self):
#         if self.income >= 25000 and self.credit_score >= 650:
#             print(self.name, "is eligible for loan.")
#         else:
#             print(self.name, "is not eligible for loan.")
    
# name = input("enter customer name: ")
# income = int(input("enter customer income: "))
# credit_score = int(input("enter customer credit score: "))

# customer = Customer(name, income, credit_score)
# customer.check_eligibility()


# Online Order Tracker................

# class Order:
#     def __init__(self, id, name, status):
#         self.id = id
#         self.name = name
#         self.status = status

# orders = []


# for i in range(2):
#     id = input("order id: ")
#     name = input("product name: ")
#     status = input("status: ")
#     orders.append(Order(id, name, status))

# update_id = input("Enter Order ID to update: ")
# new_status = input("Enter New Status: ")

# for order in orders:
#     if order.id == update_id:
#         order.status = new_status

# print("\nOrders:")
# for order in orders:
#     print(order.id, "-", order.name, "-", order.status)