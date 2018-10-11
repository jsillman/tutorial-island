import numpy as np		#importing numpy

def main():
	i = 0							#initialize i to 0
	n = 10							#and n to 10 as integers
	x = 119.0						#initialize x to 119 as a float
	
	y = np.zeros(n,dtype=float)		#array of 10 zeros as floats
	for i in range(n):				#loop from 0 to 9
		y[i] = 2.0 * float(i) + 1.0	#setting y elements to 2i+1 as floats
	
	for y_element in y:				#print each element of y
		print(y_element)
	
if __name__ == "__main__":
	main()							#run