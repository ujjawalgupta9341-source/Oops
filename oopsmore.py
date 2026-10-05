# create student name that takes name and marks of three subjects as arguement is constructed.
#create a methode to print the average.
class Student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    def average(self):
        avg=( self.marks1 + self.marks2 + self.marks3) / 3
        print("average marks=",avg)

s1=Student("yash",70,88,98)
s1.average()

#2create account class with 2 attributes-- balance and account no.
class Account:
    def __init__(self,balance,account_num):
        self.balance=balance
        self.account_num = account_num
s1=Account(9000,2509001500007653)
print("this is your acc. balance=",s1.balance)
print("this is your acc, number",s1.account_num)

#3 create method for debit, credit and printing the balance.
class Account:
    def __init__(self,balance,account_num):
        self.balance=balance
        self.account_num=account_num
    def debited(self,amount):
        self.balance-=amount
        print("net balance =",self.balance)
s1=Account(90000,2509001500009090)
s1.debited(5000)

#finished basic python
