from bill import Bill
from flat import Flatmate
from reports import PdfReport

bill_amount = float(input("Enter the bill amount: "))
bill_period = input("Enter the period: ")
bill = Bill(amount=bill_amount, period=bill_period)

user_name = input("What is your name? ")
days_in_house1 = int(input(f"Hoaw many days {user_name} are you staying in the house? "))
user_name1 = Flatmate(name=user_name, day_in_house=days_in_house1)

user_name = input("What is your name? ")
days_in_house2 = int(input(f"How many days {user_name} are you staying in the house? "))
user_name2 = Flatmate(name=user_name, day_in_house=days_in_house2)

payment = user_name1.pays(bill=bill, flatmate=user_name2)

report = PdfReport('report.pdf')
report.generate(flatmate1=user_name1, flatmate2=user_name2, bill=bill)