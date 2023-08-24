#List
a=[5,5.2,"man",False,2+3j]
print(type(a)) #used to identify the type of a
print(a)
print("Length of a is ",len(a)) #used to identify the lenght of a
print(a[1]) #list is indexable
print(a[-2]) #indexing is possible in both left to right and right to left
a.append(70) #used to add values in list
print(a)
a.append([3,4,5]) #Nested List is allowed
print(a)
a.extend([3,4,5])  #Adding multiple value in the list is possible
print(a)
a.insert(5,"world") #Insert a value in the middle of the list using index number
print(a)
print(a.pop(7)) #pop is used to take any value from a list using index
print(a)
a.remove('world') #remove is used to remove a value from a list
print(a)
a.reverse() #reverse function is used to reverse a list
print(a)
a.reverse()
print(a)
a.clear()
print(a)
b=[5,11,2,21,9,1,4]
b.sort()
print(b)
