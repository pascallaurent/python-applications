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

    def pays(self, bill):
        return bill.amount / 2


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates
    such as names, their due amount and period of the bill
    """

    def __init__(self, filename):
        self.fiilename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


bill = Bill(amount=150, period="January 2021")
jude = Flatmate(name="Jude", day_in_house=30)
pascal = Flatmate(name="Pascal", day_in_house=10)

payment = jude.pays(bill=bill)
print(payment)