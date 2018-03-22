class Trump:
	def __init__(self, love_to_mexican, hair, money):
		self.love_to_mexican = love_to_mexican
		self.hair = hair
		self.__money = money

	def get_money(self):
		# return self.money #изначально работало так
		print('Ха-ха, обойдешься без новой шубы!')
		return 'Вызвался getter'

	def set_money(self, value):
		# self.money = value #изначально работало так
		print('Хватит тырить бабки!')

	money = property(get_money, set_money)

little_Trump = Trump(False, 'Best', 4000000)

# print(little_Trump.money)
little_Trump.money = 2000000
# print(little_Trump.__money)
