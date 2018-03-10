# Алгоритм:
# 1. Несколько игроков, у каждого игрока есть скорость, нитро, 
# расход топлива, объем бака, имя, пройденная дистанция
# 2. Каждый шаг игрок выбирает просто ехать или включить нитро
# 3. Пройденная дистанция увеличиваться на величину скорости 
# или нитро, а объем бака уменьшается на величину расхода топлива
# 4. Кто раньше пройдет дистанцию, тот и выиграл


# from time import sleep

# def info(car):
# 	print(car['name'], 'проехал', str(car['distance']) + '/' + str(track))
# 	print('У', car['name'], 'осталось', car['volume'], 'топлива')

# def ride(car):
# 	car['distance'] += car['speed']
# 	car['volume'] -= car['spend']

# def turbo(car):
# 	car['distance'] += car['speed'] + car['turbo']
# 	car['volume'] -= car['spend'] + car['turbo']*1.5

# def choice(car):
# 	i = input('Выберите действие:\n\
# 		1 - просто ехать,\n\
# 		2 - включить турбо-режим.\n\
# 	Ваш выбор: ')
# 	if i == '2':
# 		turbo(car)
# 		info(car)
# 	else:
# 		ride(car)
# 		info(car)

# track = 50

# car_1 = {
# 	'name': 'Тесла',
# 	'speed': 8,
# 	'spend': 4,
# 	'volume': 40,
# 	'turbo': 4,
# 	'distance': 0 
# }

# car_2 = {
# 	'name':'Шиха',
# 	'speed': 7,
# 	'spend': 3,
# 	'volume': 35,
# 	'turbo': 5,
# 	'distance': 0 
# }

# while True:
# 	choice(car_1)
# 	sleep(3)
# 	choice(car_2)
# 	input()

class Car:
	def __init__(self, speed, spend, volume, turbo, distance):
		self.speed = speed
		self.spend = spend
		self.volume = volume
		self.turbo = turbo
		self.distance = distance

	def ride(self):
		self.distance += self.speed
		self.volume -= self.spend
	def turbo(self):
		self.distance += self.speed + self.turbo
		self.volume -= self.spend + self.turbo * 1.5
	def info(self):
 		print('проехал', str(self.distance) + '/' + str(track))
 		print( 'осталось', self.volume)

	def choice(self):
		i = input('Выберите действие:\n\
			1 - просто ехать,\n\
			2 - включить турбо-режим.\n\
		Ваш выбор: ')
		if i == '2':
			self.turbo()
			self.info()
		else:
			self.ride()
			self.info()




volga = Car(150, 30, 500, 100, 0) 
print(volga.volume)