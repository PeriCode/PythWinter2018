import random
age = int(input("Сколько тебе лет?"))

if age>=18:
	print("Добро пожаловать !!!")
	point = random.randint(0, 10)
	if point <= 5:
		print("Печалька")
	elif point >= 6 and point <= 9:
		print("Красава")
	elif point == 10:
		print("Лучший")
else:
	print("не прошел")
