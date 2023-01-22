#difference()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.difference(cities2)
print(cities3)      #print different item from cities 

#difference_update()
cities.difference_update(cities2)
print(cities)   

  