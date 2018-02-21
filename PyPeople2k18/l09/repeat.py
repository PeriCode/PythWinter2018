def rad(a=1,b=0,c=0):
	D = b*b - 4*a*c
	if D < 0:
		print('Нет действительных корней')
		return
	elif D == 0:
		print('Два совпадающих корня')
		x1 = -b/(2*a)
		return x1
	else:
		print('Два различных корня')
		x1 = (-b+D**0.5)/(2*a)
		x2 = (-b-D**0.5)/(2*a)
		return x1, x2

def sumn(*args):
	return sum(args)/len(args)

x1, x2 = rad(1,2,0)
print(x1, x2) 

print(sumn(1,2,3,4))



