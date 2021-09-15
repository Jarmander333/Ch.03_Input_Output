'''
TRAPEZOID PROGRAM
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area.

Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 18
'''

base1 = float(input("Please input base 1 of the trapezoid."))
base2 = float(input("Please input base 2 of the trapezoid."))
height = float(input("Please input the height of the trapezoid."))
bases = base1 + base2
A = bases / 2 * height
print("If the first base is " + str(base1) + ", and the second base is " + str(base2) + ", and the height is " + str(height) + ", then the area of trapezoid 1 is " + str(A))
