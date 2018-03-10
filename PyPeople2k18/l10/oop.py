# def ride():
# 	print('Врум врум')

# def nitro():
# 	print('Врум врум ' * 10)

# engine = True
# wheels = 4
# fuel = 'oil'

class Car: # описали новый класс
	engine = True # добавили свойство в класс
	wheels = 4
	fuel = 'oil'

	def ride(self): # добавили метод в класс
		print('Врум врум')

	def nitro(self, speed):
		print('Врум врум ' * speed)

	def info_fuel(self):
		print('Ваша машина использует в качестве топлива ' + self.fuel)

tesla = Car() # создали объект класса Car

tesla.nitro(20) # вызвали метод ride 

Car.ride(tesla) #аналог tesla.ride()

print(tesla.fuel) # получаем значение свойства объекта tesla
tesla.fuel = 'святая вода'
print(tesla.fuel)

shiha = Car()
print(shiha.fuel)