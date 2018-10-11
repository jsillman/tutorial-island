#this program prints the datatypes of several variables

import numpy as np

i = 10
print(type(i))				#print the datatype of i (integer)

a_i = np.zeros(i,dtype=int)	#initialize an array of ints with zeros
print(type(a_i))			#prints ndarray
print(type(a_i[0]))			#prints int64

x = 119.0
print(type(x))				#prints datatype of x (float)
y = 1.19e2
print(type(y))				#prints datatype of y (float)

z = np.zeros(i,dtype=float)	#initialize an array of floats with zeros
print(type(z))				#prints ndarray
print(type(z[0]))			#prints float64