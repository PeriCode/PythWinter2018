# Алгоритм:
# 1. Получаем список продуктов
# 2. Выбираем способ готовки
# 3. Поливаем кепчупнезом
# 4. Даем имя блюду из первых букв продуктов
import random

def cook(*args, sauce = 'кепчупнез'):
	for product in args:
		print(random.choice(action_list) + ' ' + product)
	print(cook_name(args) + ' обильно польем ' + sauce + 'ом')

def cook_name(product_list):
	name = ''
	for i in product_list:
		name += i[0:2]

	return name

action_list = ['пожарим', 'потушим', 'сварим', 'пропарим']
cook('шаурма', 'хованский', 'кола', 'деловая колбаса', 'ролтон')