'''
This program converts miles to kilometers, meters, and centimeters"
'''

'Asks user to input distance in miles'

distanceInMiles = float(input("Enter distance in miles: "))

'Set conversion for miles to kilometers, miles to meters, and miles to centimeters'

milesToKilometers = distanceInMiles * 1.60934
milesToMeters = milesToKilometers * 1000
milesToCentimeters = milesToMeters * 100

'Output miles in kilometers, meters, and centimeters'

print("Kilometers:", milesToKilometers)
print("Meters:", milesToMeters)
print("Centimeters:", milesToCentimeters)