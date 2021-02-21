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
        self.fiilename = filename

    def generate(self, flatmate1, flatmate2, bill):
        # create a pdf object
        pdf = FPDF(orientation='P', unit='pt', format='Letter')

        # adding page to the document
        pdf.add_page()

        # select the font for the doc
        pdf.set_font(family='Arial', style='B', size=16)

        # report title
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)

        # report labels
        pdf.cell(w=100, h=40, txt='Period', border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        # flatmates bill data
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=str(flatmate1.pays(bill=bill, flatmate=flatmate1)), border=1, ln=1)

        # save report as pdf file
        pdf.output(self.fiilename)


bill = Bill(amount=120, period="January 2021")
jude = Flatmate(name="Jude", day_in_house=20)
pascal = Flatmate(name="Pascal", day_in_house=25)

payment = jude.pays(bill=bill, flatmate=pascal)

report = PdfReport('report.pdf')
report.generate(flatmate1=jude, flatmate2=pascal, bill=bill)