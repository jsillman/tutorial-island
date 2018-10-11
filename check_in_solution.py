import numpy as np				#imports numpy with alias "np"

def main():						#defines main() function
	i = 0
	x = 119.0					#initializing x to 119 as a float
	for i in range(0,120):		#for loop iterates i from 0 to 119
		if i==0 or i%2==0:		#every time i is even, increase x by 3;
			x += 3
		elif i%2==1:			#every time i is odd, decrease x by 5
			x -= 5
	s = "x = %3.2e"%x			#string with the value of x in scientific notation with 2 decimal places
	print(s)					#prints

main()							#calls main() function