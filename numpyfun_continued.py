import numpy as np

x = 1.0
y = 2.0

print(np.exp(x))				#e^x
print(np.log(x))				#ln x
print(np.log10(x))				#log_10 x
print(np.log2(x))				#log_2 x

print(np.fabs(x))				#absolute value of x as a float (f.abs.)
print(np.fmin(x,y))				#min of x and y
print(np.fmax(x,y))				#max of x and y

n = 100
z = np.arange(n,dtype=float)	#make an array ranging [0.0, n-1] (a.range)
z *= 2.0*np.pi/float(n-1)		#set z range [0, 2π]
sin_z = np.sin(z)				#make an array of sin(z) values

print(np.interp(0.75,z,sin_z))	#interpolate sin(0.75)
print(np.sin(0.75))