## This Bite involves solving two problems using datetime

1. We kicked off our 100 Days of Code project on March 30th, 2017. Calculate what date we finished the full 100 days!

2. PyBites was founded on the 19th of December 2016. We're attending our first PyCon together on May 8th, 2018. Can you calculate how many days from PyBites' inception to our first PyCon meet up?

## The thinking

start_100days = 03/30/2017
end_100days = 07/08/2017
total_100days = end_100days- start_100days

pycon_start_date = 12/19/2016
pycon_together_date = 06/08/2018
pycon_total_days = pycon_together_date - pycon_start_date

## Using python

- according to python manual: A timedelta object represents a duration, the difference between two dates or times.

start_100days = 03/30/2017
end_100days = timedelta(day=100) - date(2017, 3, 30)

pycon_total_days = date(2017, 6, 8) - date(2016, 12, 9)

## Running pytest
