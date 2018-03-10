class Mail:
	# name= "Maga"
	# surname="Magomedov"
	# age=18
	# phone_number="89289999999"
	# card=False
	def __init__ (self, a, b):
		self.name = a
		self.surname = b 
	def send(self):
		print("Хватит спамить!")
men=Mail("papap","llsdl")
man=Mail("magomed","Magomedov")
print(man.name)
man.send()
Mail.send(man)
print(men.name)

man.email = 'abduev.01@gmail.com'
print(man.email)

print(men.email)