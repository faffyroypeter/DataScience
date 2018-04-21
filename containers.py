import pandas as pd

#Basic containers

#string
a = "5" 
print(a)
#string
a = "peter" 
print(a)
#bool
a = True 
print(a)

# list
mylist = [10,23,4,2]
print(mylist)
print(type(mylist))
mylist.append("peter")
print(mylist)

#list operations
mylist.count(10)

#unorderable
mylist.sort()

# accessing all elements
for item in mylist:
    print(item)

#slicing a list by specific index 
newlist = mylist[0]
print(newlist)

newlist = mylist[4]
print(newlist)

newlist = mylist[0:3]
print(newlist)
# output : [10, 23, 'bool']


newlist = mylist[0:2]
print(newlist)

# print o to 4 the element skip by second element
newlist = mylist[0:4:2]
print(newlist)

# print all from 0 index
newlist = mylist[0:]
print(newlist)

# start to 3rd element
newlist = mylist[:3]
print(newlist)

# print last element
newlist = mylist[-1]
print(newlist)

# Tuple (readonly)
mytuple = (10,23,45,"asdaf")
print(mytuple)

# accessing all elements of tuple
for item in mytuple:
    print(item)