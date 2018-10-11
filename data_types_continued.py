#this program prints the datatypes of several variables, including a list and a tuple

s = "I am a string."
print(type(s))										#prints datatype of s (string)

yes = True
print(type(yes))									#prints datatype of yes (boolean)
no = False
print(type(no))										#prints datatype of no (boolean)

alpha_list = ["a", "b", "c"]						#initialize a list alpha_list
print(type(alpha_list))								#prints datatype of alpha_list (list)
print(type(alpha_list[0]))							#prints datatype of elements of alpha_list (string)
alpha_list.append("d")								#add element "d" to the end of the list
print(alpha_list)									#prints the list

alpha_tuple = ("a", "b", "c")						#initialize a tuple alpha_tuple
print(type(alpha_tuple))							#prints datatype of alpha_tuple (tuple)

try:
	alpha_tuple[2] = "d"							#attempt to add element "d" to alpha_tuple
except TypeError:
	print("We can't add elements to tuples!" )		#catch the error by printing this message
print(alpha_tuple)									#print the tuple