# Алгоритм: 
# 1. Создаем персонажей
# 2. Даем имя, здоровье, урон
# 3. Бой есть уменьшение здоровья на величину урона
# 4. Игра идет до тех пор, пока один из игроков не потеряет все здоровье
import random

def create():
	person = {
		'hp': 100,
		'damage': 30
	}

	person['name'] = input('Введите имя персонажа: ')

	cho = int(input("""Выберите бонус
	1 - прибавка к здоровью,
	2 - прибавка к урону
"""))

	if cho == 1:
		person['hp'] += 30
	else:
		person['damage'] += 9

	return person

def fight(damager, defender):
	real_damage = damager['damage'] + random.randint(-3, 3)
	print(damager['name'], 'наносит', real_damage, 'урона', defender['name'])
	defender['hp'] -= real_damage

def health_info(person):
	print('У', person['name'], 'осталось', person['hp'], 'здоровья')
	
player_1 = create()
player_2 = create()

while True:
	fight(player_1, player_2)
	fight(player_2, player_1)
	health_info(player_1)
	health_info(player_2)

	if player_1['hp'] <= 0:
		print(player_1['name'], 'сдох')
		break

	if player_2['hp'] <= 0:
		print(player_2['name'], 'сдох')
		break

	input()

