def discr(a, b, c): # позиционные аргументы
	D = b*b - 4*a*c
	return D

def piphagor(kat_1 = 1, kat_2 = 1): # задали аргументы по умолчанию
	return kat_1*kat_1 + kat_2*kat_2

def group_list(*arg):
	for i in arg:
		print(i + ' красава')


# main_D = discr(b = 3, a = 1, c = 2)
# print(main_D)
# gip = piphagor(1, 2)
# print(gip)

group_list('Амалия', 'Валера', 'Гаджимурад', 'Карина', 'Магомедамин')