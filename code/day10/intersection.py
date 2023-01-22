#intersection()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)
#prints interesection of cities and cities2

#intersection_update
cities.intersection_update(cities2)
print(cities)
#cities is updated with intersection items 