import random #подключили библиотеку рандом

# print("Бросить кости - жмите Enter")
# input()
count_1 = random.randint(2,12) #первый игрок бросил кости
print("У вас выпало", count_1)
# print("Второй игрок делает бросок")
count_2 = random.randint(2,12) #второй игрок бросил кости
print("У второго игрока выпало", count_2)

if count_1 < count_2:
	print("Второй игрок win")
elif count_1 > count_2:
	print("Первый игрок win")
else: 
	print("draw")