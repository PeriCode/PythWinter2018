import random
h = int(input("Здравствуйте,сколько вам лет?Мне: "))
if h >= 18:
	print("Добро пожаловать!")
	throw = random.randint(0,10)
	print("*Вы бросили*", throw)
	if throw == 0:
		print("В молоко")
	elif 1 <= throw <= 5:
		print("Так себе")
	elif throw > 5 and throw <= 9:
		print("Хорошо")
	elif throw == 10:
		print("В десятку!")
else:
	print("Вы не подходите,ждём вас позже.")

