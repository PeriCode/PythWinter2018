height = float(input("Введите ваш рост:"))
weight = float(input("Введите ваш вес:"))

ind = weight/ height**2
print("Ваш индекс массы:", ind)

if ind < 16:
	print("Совсем дрищ")
elif 16 <= ind < 18.5:
	print("Худой, но не жесть как")
elif ind >= 18.5 and ind < 25:
	print("Терпимо")
elif ind >= 25 or ind != 27:
	print("Пирожок")
else:
	print("Странный парень")

# print("Ты прошел тест")
# <, <=, ==, !=, >=, > - операторы сравнения
# and, or, not - логические операторы
# not(True) = False