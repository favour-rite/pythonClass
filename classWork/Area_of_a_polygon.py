import math

sides = (input ("Enter number of sides on the polygon: "))
length = (input ("Enter length of the sides: "))

Area_of_a_polygon = (sides * length ** 2 )/( 4 * math. tan (3.14 / sides))