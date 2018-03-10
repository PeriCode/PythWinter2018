class Hero:
	def __init__(self, strength, weakness, team, side):
		self.strength = strength
		self.weakness = weakness
		self.team = team
		self.side = side

	def punch(self):
		return self.strength

	def save(self):
		print('Боже, храни Америку!')

class X_men(Hero): # унаследовал базовый класс Hero
	def fly(self):
		print('Палундра!!')

class New_X_men(X_men):
	def __init__(self, strength, weakness, team, side, teacher):
		# self.strength = strength
		# self.weakness = weakness
		# self.team = team
		# self.side = side
		super().__init__(strength, weakness, team, side)
		self.teacher = teacher

	def fly(self):
		print('Свистать всех наверх!')

superman = Hero(500, 'криптонит', 'лига справедливости', True)
logan = X_men(100, 'алкоголизм', 'люди х', True) # пропаботает конструктор базового класса
fenix = New_X_men(1000, None, None, None, 'Чарльз Ксавьер')
print(logan.team)
logan.save()
logan.fly()
# superman.fly() # нельзя вызывать метод дочернего класса для объекта базового класса
print(fenix.strength)
fenix.fly()
print(fenix.teacher)