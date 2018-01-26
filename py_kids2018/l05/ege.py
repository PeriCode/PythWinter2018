import random

score = random.randint(0,100)
print(score)
if 0 <= score <= 30:
	print("2")
elif 30 < score <= 60:
	print("3")
elif 60 < score <= 80:
	print("4")
elif 80 < score<= 100:
	print("5")
