#isdisjoint()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))
#supperset()
#superset contain all item as in orginal set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Tokyo", "Madrid", "Berlin", "Delhi"} 
print(cities.issuperset(cities3))
#issubset
s1={"ram","shyam","hari"}
s2={"ram","shyam"}
print(s2.issubset(s1))   #true is printed
#add()
s1.add("ghansyam")
print(s1)
#update()
s1.update(s2)    #update one set or list, dict with another
print(s1)
#remove()
s1.remove("ram")  #can only remove that is present otherwise erroris found
#s1.remove("yoelementnaixaina")//erro occured
#discard()
s1.discard("Yo")         #no error seen like remove
#pop()
#it removes last item but we dontknow which is last element because set is random ordered
food={"bhat","dal","chiya","alu ko achar","momo"}       
item=food.pop()     
print(item)
#del  this deletes set entirely
del food
# clear() clear all items in set and print empty set
