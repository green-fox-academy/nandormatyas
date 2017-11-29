# Saturn is missing from the planet_list
# Insert it into the correct position

planet_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]

planet_list.append('Saturn')
planet_list[5], planet_list[7] = planet_list[7], planet_list[5]


print(planet_list)