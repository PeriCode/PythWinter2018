import random
list_of_gamers = ['Султанмурад', 'Амин', 'Султан', 'Эльдар', 'Рашид', 'Саид']

name = input('Как твое имя, товарищ?')
if name in list_of_gamers:
	print('Проходите.')
	
else:
	print("В другой раз.")