# squad = input('Введи состав подразделения через запятую: ')
# squad = squad.split(', ') # разбиваем строку по символу ", " в список
# print(squad)

# list_of_man = ['Амир', 'Ибрагим', 'Артур']
# print(list_of_man)
# list_of_man = " + ".join(list_of_man) # элементы списка соединяем в строку через разделитель " + "
# print(list_of_man)

# name = input("Как твой позывной, солдат?")
# print(name in squad)
# if name in squad:
# 	print("3 наряда вне очереди")
# else:
# 	print("Сиди и жди дисбата")
# ['Курбан-черный', 'Саид-псих', 'Даниил-популист']
# name = input('Кого ищем? ')
# for i in squad:
# 	# print(i)
# 	if i == name:
# 		print("Наряд по кухне")
# 		break
# else: # работает только в том случае, если цикл завершился не командой break
# 	print('Он в самоволке')

ammo_dict = {
	'Russia': ['Концерн Калашников', 'Lobaev Arms', 'Винтарь'],
	'USA':['AR', 'Colt', 'Smith & Wesson'],
	'Germany':['Heckler & Koch', 'Mauser']
}

# for i in ammo_dict.values():
# 	print(i)

# print()
# for i in ammo_dict.keys():
# 	print(i)
# print()
# for i in ammo_dict.items():
# 	print(i)
# print()
# for i, j in ammo_dict.items():
# 	print(i, " __ ", j)

for i in range(-1, 101): # range создает список [1, 2, 3, ..., 100]
	pass

for i in range(100): # по умолчанию range стартует с 0
	pass

for i in range(100, 0, -10):
	print(i)

