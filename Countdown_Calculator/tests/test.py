# Testing whether we are getting the proper result or not from this code
# Python program to find number of days
# between two given dates
# from datetime import date
#
#
# def numOfDays(date1, date2):
#     return date2-date1
#
#
# # Driver program
# date1 = date(2018, 1, 13)
# date2 = date(2019, 2, 25)
# print(numOfDays(date1, date2), "Date")
# a = ['/', ',', '-']
# b = 'Hello world -'
# if b in a:
#     print(True)
#
from datetime import date
date_first_time = '22-11-222'.replace('-' or '.', '/')
date_list = [
    int(x) for x in date_first_time.split('/')
]
# print(date_list)
# for i in date_list:
#     print(type(i))
#
dates = date.today()
year = dates.year
# print(type(year))
date_final = date(date_list[2], date_list[1], date_list[0])
print(date_final.year)
if date_final.year > 1000:
    pass
else:
    date_final = date_final.replace(year=year)

print(date_final)