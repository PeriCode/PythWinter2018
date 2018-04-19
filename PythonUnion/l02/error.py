class MyErr(Exception):
	def __init__(self):
		print('Произошла ошибка природы!')
try:
	# a = int(input())
	# b = int(input())
	# print(a, '/', b, '= ', a/b)
	# raise
	# raise ZeroDivisionError
	raise MyErr()
except MyErr as a:
	pass
except ValueError:
	print('Произошла ошибка приведения типов!')
except ZeroDivisionError:
	print('Произошла ошибка деление на ноль!')
except Exception as e:
	print('Error: ', str(e))
else:
	print('Мы в блоке else')
finally:
	print('Мы в блоке finally')
