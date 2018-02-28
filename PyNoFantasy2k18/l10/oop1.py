# count_wheel = 4
# engine = True
# fuel = 'oil'

# def ride():
# 	print('Врум врум')

# name = 'чайка'

class Car: # описали класс Car 
	count_wheel = 4 # свойство класса
	engine = True # свойство класса
	fuel = 'oil'# свойство класса

	def ride(self, speed): # метод класса
		print('Врум врум '*speed)

seagull = Car() # создали объект класса Car
print(seagull.count_wheel, seagull.fuel) # вывели свойства объекта
seagull.ride(3) # вызвали метод

raphic = Car() # создали еще один объект класса Car
raphic.fuel = 'молитвы пассажиров' # поменяли свойство объекта
print('Рафики в качестве топлива использовали ' + raphic.fuel)
raphic.ride(5)