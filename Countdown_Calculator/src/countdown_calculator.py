# This file will handle the user which will having the user Class
# IMPORTS
from turtle import fd
from datechecker import DateDurationFinder


class User:

    def __init__(self):
        print("Enter the first date:")
        self.first_date = self.date_taker_from_user()
        print("Enter the second date:")
        self.second_date = self.date_taker_from_user()
        self.duration_of_dates = DateDurationFinder()
        return None

    def date_taker_from_user(self):
        date_from_user = [int(x)
                          for x in input("Enter the date:").split('/')]
        return date_from_user


user = User()
