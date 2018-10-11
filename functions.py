#this program prints every value of e^(x) for x ranging from 0 to one less than 
# a given value, or 9 by default

import numpy as np
import sys

def exponent(x):						#exponent(x) function: returns e^(x)
	return np.exp(x)

def show_exponent(x):					#show_exponent(x) function: prints the result of
	for i in range(x):					# e^(i) for every value of i from 0 to x-1
		print(exponent(float(i)))

def main():
	n = 10								#initialize n
	if(len(sys.argv)>1):				#if there's a command line argument,
		n = int(sys.argv[1])			# use it for n
	show_exponent(n)					#call show_exponent(n)

if __name__ == "__main__":
	main()