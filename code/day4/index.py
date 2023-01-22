colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))
print(colors.count("green"))        # counts number of time green comes in list colors
new_list=colors.copy()              # create new list by copying original list
print(new_list)
colors.append("White")              # append the new item in list colors
print(colors)                       # prints colors including white which is added
colors.insert(0,"red")              #  insert red in index 0
# before insert list  ["voilet", "green", "indigo", "blue", "green"]
# after insert list   ['red', 'voilet', 'green', 'indigo', 'blue', 'green', 'White']
#add a list to a list







colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)                            # add or extend colors list with list rainbow
print(colors)
# colors list will be updated as ['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

#you can simply concaneate two list as follow
print(colors + rainbow )