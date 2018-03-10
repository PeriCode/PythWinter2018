class Animals:
	def __init__(self, a, b, c):
		self.tail = a
		self.paws = b
		self.sound = c
	def speak(self):
		print(self.sound)
	def attack(self,victim):
		print('Атакуем'+ victim)
cat = Animals("есть", 4, "мяяяяяу или гав (когда режут)")
print(cat.paws)
cat.sound = 'ШААААА'
cat.speak()
cat.attack(' крысу')
dog = Animals('нИт', 3, 'откушу')

dog.loyalty = True
print(dog.loyalty)

# print(cat.loyalty)