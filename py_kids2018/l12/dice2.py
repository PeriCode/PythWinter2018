import random 

player_1 = {'счет': 1000}
player_2 = {'счет': 1000}

player_1['имя'] = input('Имя первого игрока: ')
player_2['имя'] = input('Имя второго игрока: ')

while True:
	player_1['ставка'] = int(input('Ставка 1-го игрока: '))
	if player_1['ставка'] > player_1['счет']:
		print('У тебя нет столько денег!')
		continue
	player_2['ставка'] = int(input('Ставка 2-го игрока: '))
	if player_2['ставка'] > player_2['счет']:
		print('У тебя нет столько денег!')
		continue

	if player_1['ставка'] > player_2['ставка']:
		print('Неровные ставки')
		player_1['ставка'] = player_2['ставка']

	if player_1['ставка'] < player_2['ставка']:
		print('Неровные ставки')
		player_2['ставка'] = player_1['ставка']


	player_1['баллы'] = random.randint(2, 12)
	player_2['баллы'] = random.randint(2, 12)

	print('Баллы 1-го:', player_1['баллы'])
	print('Баллы 2-го:', player_2['баллы'])

	if player_1['баллы'] > player_2['баллы']:
		print(player_1['имя'], 'выиграл ставку')
		player_1['счет'] += player_2['ставка']
		player_2['счет'] -= player_2['ставка']
	elif player_1['баллы'] < player_2['баллы']:
		print(player_2['имя'], 'выиграл ставку')
		player_2['счет'] += player_1['ставка']
		player_1['счет'] -= player_1['ставка']
	else:
		print('Ничья')

	print(player_1['имя'],'имеет на счету:', player_1['счет'])
	print(player_2['имя'],'имеет на счету:', player_2['счет'])

	if player_1['счет'] <= 0:
		print('Игра завершена.',player_1['имя'],'победил!')
		break

	if player_2['счет'] <= 0:
		print('Игра завершена',player_1['имя'],'победил!')
		break