# Idea
# Object Oriented Programming
# Modeling our problem as real-world objects

# Car
# What makes a car?
# 1. engine
# 2. wheels
# 3. name
# 4. doors


#  Car
# 1. engine - v8
# 2. wheels - 4
# 3. name - Ferrari
# 4. doors - 2


# 1. engine - v4
# 2. wheels - 4
# 3. name - Alto
# 4. doors - 4


#  Car -> blueprint | Class blueprint object


# class Car:
#     def __init__(
#         self, name, engine, wheels, doors
#     ):  # creating object calls init (constructor)
#         self.name = name
#         self.engine = engine
#         self.wheels = wheels
#         self.doors = doors

#     # Instance method
#     def horn(self):
#         return f"{self.name} says Vroom Vroom"


# ferrari = Car("Ferrari", "v8", 4, 2)  # object
# alto = Car("Alto", "v4", 4, 4)  # object
# sumo = Car("Suma", "v12", 4, 5)
# thar = Car("Thar", "v4", 4, 4)

# print(ferrari.name, ferrari.wheels)
# print(alto.name, alto.doors)
# print(sumo.engine, sumo.wheels)
# print(thar.name, thar.engine)
# print(type(ferrari))  # <class '__main__.Car'>
# print(ferrari.horn())

# Encapsulation: properties + action(logic)

# Task 1
# class BankAcc:

#     interest_rate = 0.02 # class variable
#     total_accounts = 0

#     @classmethod
#     def get_total_no_accounts(cls):
#         return f"Total number of accounts: {cls.total_accounts}"

#     @classmethod
#     def update_interest_rate(cls, rate):
#         cls.interest_rate = rate

#     def __init__(self, acc_no, name, balance):
#         self.acc_no = acc_no
#         self.name = name
#         self.balance = balance
#         BankAcc.total_accounts += 1


#     def display_balance(self):
#         return f"The current balance is ₹.{self.balance:,}"

#     def withdraw(self):
#         amount = float(input("Enter the amount to be Withdrawed: "))
#         if amount > self.balance:
#             return "Insufficient Balance!"
#         else:
#             self.balance -= amount
#             return f"Withdrawal Successful! Your new balance is ₹.{self.balance:,}"

#     def deposit(self):
#         amount = float(input("How much do you want to Deposit? "))
#         self.balance += amount
#         return f"The new balance is ₹.{self.display_balance()}"


#     def interest(self):
#         accumulated_interest_amt = self.balance * BankAcc.interest_rate
#         self.balance += accumulated_interest_amt
#         return f"Interest received. ₹{accumulated_interest_amt}"


# amisha = BankAcc(101, "Amisha", 50_000)
# mathesh = BankAcc(102, "Mathesh", 70_000)
# sai = BankAcc(103, "Sai", 65_000)

# print(f"Account No : {amisha.acc_no}, Name : {amisha.name}, Balance : Rs.{amisha.balance}")
# print(f"\n Account No : {mathesh.acc_no}, Name : {mathesh.name}, Balance : Rs.{mathesh.balance}\n")
# print(f"\n Account No : {sai.acc_no}, Name : {sai.name}, Balance : Rs.{sai.balance}\n")

# Task 2
# print(amisha.display_balance())

# Task 3
# print(mathesh.withdraw())

# Task 4
# print(sai.deposit())

# Task 5 - interest rate
# print(sai.interest())

# Task 6 get_total_no_accounts() , update_interest_rate()
# print(BankAcc.get_total_no_accounts())


# Static method vs Class method | Both Decorators!
# Super charge to the normal method
# Static method


# class Circle:
#     pi = 3.14

#     def __init__(self, radius):
#         self.radius = radius

#     @staticmethod # --> no cls, self | normal function
#     def perimeter(radius):
#         return 2 * Circle.pi * radius

#     @classmethod # --> Can use class variables
#     def from_diameter(cls, diameter):
#         # Calculate radius from diameter
#         radius = diameter / 2
#         # Return an instance of Circle using the calculated radius
#         return cls(radius)

#     def calculate_area(self):
#         return Circle.pi * self.radius**2


# # Normal function but inside class | no access to self
# print(Circle.perimeter(2))

# # Instance method
# circle1 = Circle(4)
# print(circle1.calculate_area())

# # Class method - to construct the object
# circle_from_dia = Circle.from_diameter(10) # 10 -> Dia
# print(circle_from_dia.calculate_area())  # Output: 78.5


# Access Specifier
# Private, -> __balance (double underscore)
# Public,
# Protected -> _balance (single underscore)

# class BankAcc:

#     __interest_rate = 0.02 # class variable
#     __total_accounts = 0

#     @classmethod
#     def get_total_no_accounts(cls):
#         return f"Total number of accounts: {cls.__total_accounts}"

#     @classmethod
#     def update_interest_rate(cls, rate):
#         cls.__interest_rate = rate

#     def __init__(self, acc_no, name, balance):
#         self.acc_no = acc_no
#         self.name = name
#         self.__balance = balance # RENAME EVERYWHERE -> F2
#         BankAcc.__total_accounts += 1


#     def display_balance(self):
#         return f"The current balance is ₹.{self.__balance:,}"

#     def withdraw(self):
#         amount = float(input("Enter the amount to be Withdrawed: "))
#         if amount > self.__balance:
#             return "Insufficient Balance!"
#         else:
#             self.__balance -= amount
#             return f"Withdrawal Successful! Your new balance is ₹.{self.__balance:,}"

#     def deposit(self):
#         amount = float(input("How much do you want to Deposit? "))
#         self.__balance += amount
#         return f"The new balance is ₹.{self.display_balance()}"


#     def interest(self):
#         accumulated_interest_amt = self.__balance * BankAcc.__interest_rate
#         self.__balance += accumulated_interest_amt
#         return f"Interest received. ₹{accumulated_interest_amt}"


# amisha = BankAcc(101, "Amisha", 50_000)
# mathesh = BankAcc(102, "Mathesh", 70_000)
# sai = BankAcc(103, "Sai", 65_000)

# print(f"Account No : {amisha.acc_no}, Name : {amisha.name}, Balance : Rs.{amisha.balance}")
# print(f"\n Account No : {mathesh.acc_no}, Name : {mathesh.name}, Balance : Rs.{mathesh.balance}\n")
# print(f"\n Account No : {sai.acc_no}, Name : {sai.name}, Balance : Rs.{sai.balance}\n")

# Task 2
# print(amisha.display_balance())

# Task 3
# print(mathesh.withdraw())

# Task 4
# print(sai.deposit())

# Task 5 - interest rate
# print(sai.interest())

# Task 6 get_total_no_accounts() , update_interest_rate()
# print(amisha.display_balance())

# Inheritance


# Task 5
# class SavingsAccount:
#     __interest_rate = 0.05

#     def __init__(self, acc_no, name, balance):
#         self.__acc_no = acc_no
#         self.__name = name
#         self.__balance = balance

#     def apply_interest(self):
#         interest_amount = self.__balance * SavingsAccount.__interest_rate
#         self.__balance += interest_amount
#         return f"Balance after interest: ₹{self.__balance:,.2f}"

#     def get_balance(self):
#         return f"Current balance: ₹{self.__balance:,.2f}"


# sabesh = SavingsAccount(131, "Sabesh", 80000)
# print(sabesh.apply_interest())
# print(sabesh.get_balance())


# common across objects - class variable (cls)
# unique across objects - instance variable (self)


# Task 6
# class CurrentAccount:
#     transaction_fee = 10

#     def __init__(self, acc_no, name, balance):
#         self.acc_no = acc_no
#         self.name = name
#         self.balance = balance

#     def apply_transaction_fee(self):
#         if self.balance < CurrentAccount.transaction_fee:
#             print("Insufficient funds for transaction fee.")
#         else:
#             self.withdraw(CurrentAccount.transaction_fee)

#     def withdraw(self, amount):
#         if amount > self.balance:
#             return "Insufficient Balance!"
#         else:
#             self.balance -= amount
#             return f"Withdrawal Successful! Your new balance is ₹{self.balance:,}"

#     def get_balance(self):
#         return f"Your balance is: ₹{self.balance:,}"


# tanishq = CurrentAccount(132, "Tanishq", 90000)

# print(tanishq.withdraw(1000))
# tanishq.apply_transaction_fee()
# print(tanishq.get_balance())

# # # Task 6
# # # withdraw - per_transaction_fee - 10 Rupee
# class CurrentAccount(Bank4):
#     per_transaction_fee = 10

#     # Polymorphism: method overloading
#     def withdraw(self, amount):
#         total_amount = amount + CurrentAccount.per_transaction_fee
#         return super().withdraw(total_amount)


# tanishq = CurrentAccount(132, "Tanishq", 90_000)

# print(tanishq.withdraw(1_000))
# print(tanishq.withdraw(10_000))
# print(tanishq.display_balance())

# common across objects - class variable  (cls)         - no. of eyes
# unique across objects - instance variable (self)      - size of nose


# # Inheritance
# class Animal:
#     def __init__(self, name):
#         self._name = name

#     # methods / attributes
#     def speak(self):
#         return "Some sound"


# class Dog(Animal):
#     def __init__(self, name, speed):
#         super().__init__(name)  # Base class constructor
#         self.__speed = speed

#     def run(self):
#         return "🐶 wags tail!!"

#     # Polymorphism:  Method overriding
#     def speak(self):
#         return "Woof!! 🐕"

#     def speed_bonus(self):
#         return f"{self._name} is running at {self.__speed * 2}Km/hr"


# toby = Animal("toby")
# print(toby.speak())
# # print(toby.run())

# maxy = Dog("maxy", 20)
# # print(maxy._name)
# print(maxy.run())
# print(maxy.speak())
# # print(maxy.__speed)
# print(maxy.speed_bonus())


# Magic Methods
# __init__ -> Dunder Method
# __str__ -> To String Conversion
# __repr__ -> Debugging
