#this program demonstrates several functions of the list class

x = [0.0, 3.0, 5.0, 2.5, 3.7]
print(type(x))						#prints datatype of x (list)

x.pop(2)							#remove the 3rd element of x (5.0)
print(x)

x.remove(2.5)						#remove the element 2.5 (index 2)
print(x)

x.append(1.2)						#add a new element to the end (1.2)
print(x)

y = x.copy()						#make a copy of x's current state (y)
print(y)

print(y.count(0.0))					#print the number of elements equal to 0.0 (1)

print(y.index(3.7))					#print the index of the element 3.7 (2)

y.sort()							#sort the list y by value
print(y)

y.reverse()							#reverse the order of elements in list y
print(y)

y.clear()							#remove all elements from y
print(y)