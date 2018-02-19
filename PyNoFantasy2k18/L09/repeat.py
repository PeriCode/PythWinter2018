def a(*args):
	return sum(args) / len(args)

def q(a = 0, b = 0, c = 0):
	D = b*b - 4*a*c
	if D < 0:
		print('Действительных корней нет')
		return
	elif D == 0:
		print('2 совпадающих корня')
		X = -b/(2*a)
		return X
	else:
		print('2 различных корня')
		x1 = (-b + D**0.5)/(2*a)
		x2 = (-b - D**0.5)/(2*a)
		return x1, x2
# print(q(1,2,1))
y1, y2 = q(1,2,0)
print(y1, y2)
print(a(2, 4, 5, 6, 8))
