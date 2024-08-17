# tuples are unchangable

planets_list = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']

planets_list[1] = "Arun"

print(planets_list)
print(type(planets_list))

#tuples

planets = ('Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune')
print(type(planets))
print(planets[:5])

for planet in planets:
    print(planet, end=" ")
#planets[5]="Arun"