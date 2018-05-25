#обработка list

a = [1,2,3,4,[5,6,6,6,[5,[5,[5,6]]],6,6,6],7,[8,[10,[11,[5,[[5,6],6]],15]]]]


def list_int_to_str(a):
	b = []
	for i in a:
		if type(i) == list:
			b.append(list_int_to_str(i))
		else:
			b.append(str(i))
	return b


def list_to_long(a):
	b = []
	for i in a:
		if type(i) == list:
			for k in list_to_long(i):
				b.append(k)
		else:
			b.append(str(i))
	return b

print (list_int_to_str(a))
print (list_int_to_str(a))
print (list_int_to_str(a))
print (list_int_to_str(a))
print (list_int_to_str(a))

print (list_to_long(a))
print (list_to_long(a))
print (list_to_long(a))
print (list_to_long(a))
print (list_to_long(a))

