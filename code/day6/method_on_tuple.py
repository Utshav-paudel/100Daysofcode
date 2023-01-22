# since tuples are immutable there are no any methods on tuple
tup=("ram","hari","ramesh","shyamlal")
# but we can make changes in tuple by converting it to list
change_tup=list(tup)
print(type(change_tup))
#<class 'list'> is printed as output
#after this we can apply any list method we want
#but few method that work on tuple without chaning them are
print(len(tup))
print(tup.index("ram"))