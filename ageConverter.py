'''
This program asks a user to enter their age in years and displays the age in months, days, hours, and seconds
'''

'Prompts user to enter age in years'
y = float(input("Enter age in years: "))

'Variables and functions for months, days, hours, and seconds'
m = y * 12
d = y * 365
h = d * 24
s = h * 3600

'Output variables as age in months, days, hours, and seconds'
print(y, "Years")
print (m, "Months")
print (d, "Days")
print (h, "Hours")
print (s, "Seconds")
