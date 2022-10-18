# This file will handle the user which will having the user Class
# IMPORTS
from datechecker import DateDurationFinder


class User:

    def __init__(self):
        self.first_date = self.date_taker_from_user()[0]
        self.second_date = self.date_taker_from_user()[1]
        print(self.first_date, self.second_date)
        self.duration_of_dates = DateDurationFinder()
        return None

    def date_taker_from_user(self):

        return [0, 1]


user = User()
