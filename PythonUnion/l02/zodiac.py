# Вводятся два числа: число и месяц. 
# В зависимости от введеных чисел выводится 
# соответствующий знак зодиака.
# В случае некорректного ввода выводится
# сообщение об ошибке и предлагается 
# ввести числа повторно!

class InputErr(Exception):
	pass

while True:
	try:
		a = int(input('В какой день ты родился '))
		b = int(input('В какой месяц ты родился '))
		if (a < 1 or a > 30) or (b < 1 or b > 12):
			raise InputErr()
		else:
			print('Вы овен')
			break
	except InputErr:
		print('Ошибка ввода. Попробуйте снова')
	except Exception as e:
		print('Error ' + str(e))
