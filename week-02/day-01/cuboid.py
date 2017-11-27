# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000

length = int(input('Length: '))
width = int(input('width: '))
height = int(input('height: '))

surface = (length + width + height) * 2
volume = length * width * height

print('surface area:', surface)
print('volume: ', volume)