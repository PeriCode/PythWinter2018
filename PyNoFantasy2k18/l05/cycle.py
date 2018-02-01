i = 0
while i <= 12:
	# print(i)
	i += 1

# name = ""
# while name != 'Алибула':
# 	print("Пока не придет Алибула я не остановлюсь")
# 	name = input("Введи имя: ")

while True:
	print("Как получить число пи?")
	text = input()
	if text == 'Стоп':
		break	
	if text == 'Знаю':
		continue # restart current cycle 
	print("Раздели длина на диаметр круга")