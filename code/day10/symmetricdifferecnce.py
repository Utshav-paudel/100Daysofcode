#symmetric_difference()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)     #different items from two sets get printed

#symmetric_difference_update()
cities.symmetric_difference_update(cities2)
print(cities)   #cities is updated with the different items from two sets
