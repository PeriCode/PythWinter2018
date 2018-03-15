class Phones:
	def __init__(self, price, display, camera):
		self.price = price
		self.display = display
		self.camera = camera

	def call(self):
		print('Ало, это милиция!')

	def make_photo(self):
		print('Я сделал снимок')

class Iphone(Phones):
	def __init__(self, price, display, camera, apple = True):
		super().__init__(price, display, camera)
		self.apple = apple

	def make_photo(self):
		print('Я сделал снимок с айфона')


xiomi = Phones(5000, 720, 2.5)
xiomi.make_photo()

iphone_x = Iphone(50000, 1920, 10.5)
iphone_x.make_photo()