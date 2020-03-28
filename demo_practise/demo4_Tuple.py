
# List
mylist = [1, 2, 3, 4, 5]
print(mylist)
print(len(mylist))
print(mylist[0])

# Tuple
mytuple = (1, 2, 3, 4, 5)
print(mytuple)
print(len(mytuple)) 
print(mytuple[0])


print(dir(mylist))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~")
print(dir(mytuple))

# list is mutable
# tuple is inmutble

mylist.remove(2)
print(mylist)

#mytuple.remove(2)
print(mytuple)
