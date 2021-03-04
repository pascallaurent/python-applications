from bill import Bill
from flat import Flatmate
from reports import PdfReport
from fileupload import FileUpload


bill_amount = float(input("Enter the bill amount: "))
bill_period = input("Enter the period: ")
bill = Bill(amount=bill_amount, period=bill_period)

# user 1
user_name = input("What is your name? ")
days_in_house = int(input(f"Hoaw many days {user_name} are you staying in the house? "))
flatmate1 = Flatmate(name=user_name, day_in_house=days_in_house)

# user 2
user_name = input("What is your name? ")
days_in_house = int(input(f"How many days {user_name} are you staying in the house? "))
flatmate2 = Flatmate(name=user_name, day_in_house=days_in_house)

# Generate billing report
report = PdfReport(filename=f"{bill.period}.pdf")
report.generate(flatmate1=flatmate1, bill=bill, flatmate2=flatmate2)

# upload file
fileurl = FileUpload(filepath=f"{bill.period}.pdf")
print(fileurl.upload())
