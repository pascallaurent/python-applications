import os
import webbrowser

from fpdf import FPDF


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
        pdf.image(name="files/house.png", w=40, h=40)

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

        # change to the files directory
        os.chdir('files')

        # save report as pdf file
        pdf.output(self.filename)

        # open report in the browser
        webbrowser.open_new(self.filename)