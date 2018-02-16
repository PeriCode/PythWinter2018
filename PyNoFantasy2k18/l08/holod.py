# Алгоритм:
# 1. Составляем список продуктов
# 2. Выбираем как будем готовить
# 3. Поливаем все майонезом
# 4. Дать название блюду
import random

product_list = ['Авокадо', 'Фейхуа', 'Докторская колбаса',
'Живой осьминог', 'Васаби', 'Повесевшаяся мишь', 'Лапки пауков', 'Хвост яшерицы' , 'Пингвин']

action_list = ['пожарить', 'потушить', 'запечь', 
'сварить']

def cook(args, main_ingr = 'майонез'):
	for product in args:
		print(random.choice(action_list) + ' ' + product)

	print(make_name(args) + ' обильно польем ' + main_ingr + 'ом')

def make_name(args):
	name = []
	for product in args:
		name += product[0]

	name = ''.join(name).lower()
	return name

cook(product_list)

