#this program explores the dictionary class in python

ex_dict = {
	"class"			:	"Astr 119",
	"prof"			:	"Brant",
	"awesomeness"	:	10
}
print(type(ex_dict))					#prints datatype of ex_dict (dictionary)

course = ex_dict["class"]
print(course)							#prints the value under the key "class" in ex_dict

ex_dict["awesomeness"] += 1				#increase value of awesomeness

print(ex_dict)

for x in ex_dict.keys():				#print each element of ex_dict, iterating through keys
	print(x,ex_dict[x])