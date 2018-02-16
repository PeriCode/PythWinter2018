import random

def create():
	person = {
		'hp':100,
		'damage':30
	}
	person['name'] = input('Имя первого игрока: ')
	cho = int(input("""Выберите бонус: 
	1 - прибавка к урону,
	2 - прибавка к здоровью.
	"""))
	if cho == 1:
		person['damage'] += 7
	else:
		person['hp'] += 30

	return person

def fight(attacker, victim):
	print(attacker['name'],'наносит удар по', victim['name'])
	victim['hp'] -= attacker['damage'] + random.randint(-3,3)

def info_health(person):
	print('У', person['name'], 'осталось', person['hp'], 'жизней')

player_1 = create()
player_2 = create()

while True:
	fight(player_1, player_2)
	fight(player_2, player_1)

	info_health(player_1)
	info_health(player_2)	

	if player_1['hp'] <= 0:
		print(player_1['name'], 'сдох первым. Очень жаль')
		break
	if player_2['hp'] <= 0:
		print(player_2['name'], 'сдох первым. Очень жаль')
		break

	input()


