class Weapon:
	def __init__(self, country, damage, distance):
		self.country = country
		self.damage = damage
		self.distance = distance

	def make_damage(self):
		print("Нанесли " + str(self.damage) + ' врагу')

	def rusting(self, time):
		while time >= 0:
			print('Гнию')
			time -= 1

class Guns(Weapon):
	def sound(self):
		print('Бабах')

class Revolver(Guns):
	def __init__(self, country, damage, distance, drum, caliber):
		super().__init__(country, damage, distance)
		self.drum = drum
		self.caliber = caliber

	def sound(self):
		print('Тарарах-тарах')
country = input('Введите страну-производителя: ')
water_gun = Weapon(country, int(input('Введите урон: ')), 5)
water_gun.make_damage()
desert_eagle = Guns('USA', 30, 50)
print(desert_eagle.country)
desert_eagle.sound()
# water_gun.sound()

smith_and_wesson = Revolver('USA', 25, 50, True, '44')
smith_and_wesson.sound()
smith_and_wesson.rusting(3)
print(smith_and_wesson.caliber)
