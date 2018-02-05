# Алгоритм игры в кости: 
# 1. Игроки представляются
# 2. Каждому игроку выдаются деньги
# 3. Каждый игрок делает ставку
# 4. Бросаются кубики
# 5. Победитель получает ставку проигравшего
# проигравший теряет свою ставку
# 6. Игра продолжается до тех пор, пока
# один из игроков не станет банкротом

import random 

player_1 = {'счет': 1000}
player_2 = {'счет': 1000}

player_1['имя'] = input('Имя первого игрока: ')
player_2['имя'] = input('Имя второго игрока: ')

player_1['ставка'] = int(input('Ставка 1-го игрока: '))
player_2['ставка'] = int(input('Ставка 2-го игрока: '))

player_1['баллы'] = random.randint(2, 12)
player_2['баллы'] = random.randint(2, 12)

print('Баллы 1-го:', player_1['баллы'])
print('Баллы 2-го:', player_2['баллы'])

if player_1['баллы'] > player_2['баллы']:
	print('Первый игрок выиграл ставку')
	player_1['счет'] += player_2['ставка']
	player_2['счет'] -= player_2['ставка']
elif player_1['баллы'] < player_2['баллы']:
	print('Второй игрок выиграл ставку')
	player_2['счет'] += player_1['ставка']
	player_1['счет'] -= player_1['ставка']
else:
	print('Ничья')

print('У первого игрока на счету :', player_1['счет'])
print('У второго игрока на счету :', player_2['счет'])
