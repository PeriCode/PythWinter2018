def discr(a = 0, b = 0, c = 0):
	D = b*b - 4*a*c
	return D 

def list_group(*args):
	for i in args:
		print(i + ' красава')
	# return args


# print(discr(b = 1, c = 2, a = 3))
# print(discr()) 
list_group('Казбек', 'Артур', 'Светлана')

