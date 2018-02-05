# list_of_visits = list_of_visits.split(', ')
# man_list = ['Малик', 'Магомедамин', 'Рашид']
# print(man_list)
# print(' => '.join(man_list))

# print(list_of_visits)

# name = input('Представьтесь пожалуйста: ')
# print(name in list_of_visits)
# if name in list_of_visits:
# 	print('Добро пожаловать!')
# else:
# 	print('Добро гулять!')
# list_of_visits = input('Введите список гостей через запятую:').split(', ')
# # ['Магомед', 'Рашид', 'Карина']
# # k = 1
for i in list_of_visits:
	# print(str(k) + ')', i)
 	# k += 1
 	if i == 'Эльдар':
 		print("Мы нашли его. По машинам.")
 		break
else:
	print('Не наш клиент')

# range(1, 100) = [1, 2, 3, ... , 99]

# for i in range(60, 0, -10): 
# 	print(i)


# dict_of_prog_lang = {
# 	'Java': 'Android, Desktop',
# 	'C': 'Hardware, Desktop',
# 	'Pascal': None,
# 	'C#': 'Desktop, Unity'
# }


# lang = input("Введи название языка: ")
# work = input("Где нужен :")
# for i in dict_of_prog_lang.items(): # items - список пар, keys - список ключей, values - список значений
# 	pass

# if zip(lang, work) in [('Java','Android, Desktop'), ('C', 'Hardware, Desktop')]:
# 	print('Ура')

# for i in zip(1, 2):
# 	print(i)