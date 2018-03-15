class Putin:
	def __init__(self, hair, time, promises):
		self.hair = hair
		self.__time = time
		self.promises = promises

	def make_promises(self):
		print('Обещаю' + self.promises)

	def getter(self): # описываем метод доступа к свойству 
		return 'Шиш тебе!'

	def setter(self, value): # описываем метод, который меняет значение свойства
		print('Сколько хочу - столько и правлю!')

	time = property(getter, setter) # связка свойства и геттера с сеттером

clon_1 = Putin(None, '(><)', input('Предвыборные обещания: '))

print(clon_1._Putin__time)
clon_1.time = 0