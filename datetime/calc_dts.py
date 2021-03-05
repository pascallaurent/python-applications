from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    end_100days_date = timedelta(days=100) + start_100days

    return str(end_100days_date)


def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""
    pybites_founded_date = date(2016, 12, 19)
    pycon_total_days = (pycon_date - pybites_founded_date).days

    return pycon_total_days


if __name__ == '__main__':

    print(get_hundred_days_end_date())
    print(get_days_between_pb_start_first_joint_pycon())