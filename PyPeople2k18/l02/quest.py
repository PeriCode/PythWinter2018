print("""Вы очнулись в трюме космического корабля, вы - космическая пельмешка. 
Что вы будете делать:
	1. Кушаете себя.
	2. Осматриваетесь в поисках оружия.
	3. Пытаетесь выйти в дверь.
	""")
act = int(input("Вы выбрали: "))

if act == 1:
	print("Это было опрометчиво, но вкусно. Игра проиграна.")

elif act == 2:
	print("""В результате осмотра вы находите бластер. 
Что же делать дальше?
	1. Пальнуть в себя! Жизнь пельменя была невыносимой.
	2. Выстрелить в Сулеймана, который прятался в это время под столом.
	3. Выстрелить в дверной замок. 
	""")
	act = int(input("Вы выбрали: "))
	if act == 1:
		print("Вы переродились в облике симпатичной, румяной, курзешкой")
	elif act == 2:
		print("Сулейман визжит как поросенок и отправляется в Страну Вечной Охоты на белогвардейцев")
	elif act == 3:
		print("Дверь открылась, а за ней ... Навальный!")

elif act == 3:
	print("Дверь вела в открытый космос. Жизнь пельменя окончена")

else:
	print("Ты ошибся, глупец")