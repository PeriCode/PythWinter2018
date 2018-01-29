weight = float(input("Введи свой вес:"))
height = float(input("Введи свой рост:"))
index = weight / (height * height)
print("Ваш индекс массы:", index)

if index < 16:
	print("Дефицит массы")
elif 16 <= index < 18:
	print("Недостаток массы тела")
elif 18 <= index < 25:
	print("Норма веса")
elif  25 <= index < 30:
	print("Излишек массы тела")
elif index >= 30:
	print ("Все плохо")

