'''
This program calculates the area of a room to determine
the amount of flooring required in feet and outputs
it in sqaure yards
'''

'Variables for users to input length and width of room in feet'
lengthOfRoom = float(input("Enter the length of the room in feet: "))
widthOfRoom = float(input("Enter the width of the room in feet: "))

'Equation to calculate area of room'
areaOfRoomFeet = lengthOfRoom * widthOfRoom

'Convert area from feet to yards'
areaOfRoomYards = areaOfRoomFeet / 9

'Prints a statement with the output in sqare yards'
print("The area of the room is", areaOfRoomYards, "square yards.")
