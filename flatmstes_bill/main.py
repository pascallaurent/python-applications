import webbrowser

from fpdf import FPDF

class Bill:
    """
    Data that contains data about a bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person who lives in the
    flat and pays a share of the bill
    """

    def __init__(self, name, day_in_house):
        self.name = name
        self.day_in_house = day_in_house

    def pays(self, bill, flatmate):
        weight = self.day_in_house / (self.day_in_house + flatmate.day_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates
    such as names, their due amount and period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate_pay1 = str(round(flatmate1.pays(bill=bill, flatmate=flatmate2), 2))
        flatmate_pay2 = str(round(flatmate2.pays(bill=bill, flatmate=flatmate1), 2))

        # create a pdf object
        pdf = FPDF(orientation='P', unit='pt', format='Letter')

        # adding page to the document
        pdf.add_page()

        # add image
        pdf.image(name="house.png", w=40, h=40)

        # select the font for the doc
        pdf.set_font(family='Arial', style='B', size=24)

        # report title
        pdf.cell(w=0, h=80, txt='Flatmates Bill', align='C', ln=1)

        # report labels
        pdf.set_font(family='Arial', style='B', size=12)
        pdf.cell(w=100, h=40, txt='Period')
        pdf.cell(w=150, h=40, txt=bill.period, ln=1)

        # flatmates bill data
        pdf.set_font(family='Arial', size=12)
        pdf.cell(w=100, h=40, txt=flatmate1.name)
        pdf.cell(w=150, h=40, txt=flatmate_pay1, ln=1)

        pdf.cell(w=100, h=40, txt=flatmate2.name)
        pdf.cell(w=150, h=40, txt=str(flatmate_pay2), ln=1)

        # save report as pdf file
        pdf.output(self.filename)

        # open report in the browser
        webbrowser.open(self.filename)

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