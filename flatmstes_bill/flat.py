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