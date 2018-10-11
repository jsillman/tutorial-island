#this program shows how to catch exceptions thrown by the program, either specific or generally

try:
	print(a)							#throws an exception because a is not defined
except:
	print("a is not defined!")			#what to do when the exception is thrown

try:
	print(a)							#throws same exception
except NameError:
	print("a is still not defined")		#what to do if the exception thrown is specifically a NameError
except:
	print("Something else went wrong")	#what to do if it's any old exception

print(a)								#the program will stop since this exception is not caught