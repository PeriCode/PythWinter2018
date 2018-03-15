class MagicPerson:
	def __init__(self, favorite_weapon, areal, damage, hp):
		self.favorite_weapon = favorite_weapon
		self.areal = areal
		self.damage = damage
		self.hp = hp

	def fight(self):
		print('Тыдыщ'*self.damage)

class Elf(MagicPerson):
	def __init__(self, favorite_weapon, areal, damage, hp, ears = 'острые'):
		super().__init__(favorite_weapon, areal, damage, hp)
		self.ears = ears

	def fight(self):
		print('Вжух'*self.damage)

class Ork(MagicPerson):
	def __init__(self, favorite_weapon, areal, damage, hp, skin = 'зеленая'):
		super().__init__(favorite_weapon, areal, damage, hp)
		self.skin = skin

	def fight(self):
		print('Хрясь'*self.damage)

gendalf = MagicPerson('Посох', 'Средиземье', 3, 1000)
legalas = Elf('Лук', 'Лориэн', 4, 500)
azoc = Ork('Топор', 'Политех', 2, 700)

gendalf.fight()
legalas.fight()
azoc.fight()