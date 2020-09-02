2.Write a Python program to calculate number of
days between two dates.

from datetime import date
d0 = date(2020, 8, 18)
d1 = date(2020, 9, 26)
delta = d1 - d0
print("Total difference in days is",delta.days)