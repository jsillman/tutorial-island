#this program uses if-elif-else statements to check the value of a variable

def flow_control(k):										#flow_control(k) function:
	s = ""													# sets a string s to a message
	if(k==0):												# describing the value of k,
		s = "Variable k = %d equals 0."%k					# then prints the message.
	elif(k==1):
		s = "Variable k = %d equals 1."%k
	else:
		s = "Variable k = %d does not equal 0 or 1."%k
	
	print(s)

def main():													#main() function: tests
	i = 0													# flow_control(k) for values
	flow_control(i)											# of 0, 1, and 2.
	i = 1
	flow_control(i)
	i = 2
	flow_control(i)

if __name__ == "__main__":
	main()