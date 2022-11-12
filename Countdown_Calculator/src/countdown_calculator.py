# This file will handle the user which will having the user Class
# IMPORTS
from datetime import date, datetime


class DateDurationFinder:
    def __init__(self, date1, date2):
        self.date1, date2 = date1, date2

        print(date1)
        print(date2)


class User:

    def __init__(self):
        print("Enter the first date:")
        self.first_date = self.date_taker_from_user()
        print("Enter the second date:")
        self.second_date = self.date_taker_from_user()
        self.duration_of_dates = DateDurationFinder(self.first_date, self.second_date)

    @staticmethod
    def date_taker_from_user():
        date_first_time = input("Enter the date: ").replace('-' or '.', '/')
        date_list = [
            int(x) for x in date_first_time.split('/')
        ]
        today_date = datetime.today()
        date_from_user = date(date_list[2], date_list[1], date_list[0])
        date_today = date.today()
        year = date_today.year
        date_from_user = date_from_user.replace(year=int(year))
        return date_from_user


user = User()
