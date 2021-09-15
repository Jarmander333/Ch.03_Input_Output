# Sign your name: Joseph Jarman
# In all the short programs below, do a good job communicating with your end user!

import math
pi = "3.14159265358975323"

# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.

name = input("Enter your name: ")
print("\n\nGood day " + name + ", thanks for using my program!")

# 2.) Write a program where a user enters a base and height and you print the area of a triangle.

base = float(input("Enter the base of a triangle, " + name + ": "))
height = float(input("Enter the height of a triangle, " + name + ": "))
area = float(base * height / 2)

print(name + ", if the base of a triangle is " + str(base) + ", and the height is " + str(height) + ", then the area will be " + str(area))

# 3.) Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
# 2(pi)r
r = input(name + ", please enter the radius of a circle! (Remember that radius is half of the diameter...)")
C = 2*float(pi)*float(r)
print("The circumference (C) is " + str(C) + "!")

# 4.) Ask a user for an integer and then print the square root.

num = int(input(name + ", enter an integer: "))
sqrt = math.sqrt(num)
print(name + ", the square root of that is, " + str(sqrt))

# 5.) Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.

print("May the mass times acceleration be with you!' because F=ma!\n")
m = float(input("\nWhat is the mass: "))
a = float(input("\nWhat is the acceleration: "))
F = m*a
print(name + ", the force is " + str(F))
