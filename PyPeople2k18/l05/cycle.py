# i = 1
# while i <= 100:
# 	print(i)
# 	i += 1 # i = i + 1 

name = ''
# while name != 'Ахмед':
# 	print('Я ищу Ахмеда')
# 	name = input("Как тебя зовут?")


while True: 
	print("\nЯ работаю. Я всегда работаю.")
	name = input("Скажи что-нибудь ")
	if name == 'Хватит работать':
		break # прерываем цикл
	if name == 'Сделай паузу':
		continue # прерываем текущую итерацию
	print("Завтра выходной")