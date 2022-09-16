'''
This program converts human years to dog years
'''

'Creating input variables'

dogName = str(input("Enter dog's name: "))
dogAgeHumanYears = float(input("Enter dog's age in human years: "))

'Setting the conversion from human to dog years. 1 human year = 7 dog years'

dogAgeDogYears = dogAgeHumanYears * 7

'Output dog name and dog age in dog years'

print(dogName, "is", dogAgeDogYears, "years old in dog years")