def summ(): # описали функцию без параметров
	a = int(input('1-е число: '))
	b = int(input('2-е число: '))
	print(a + b)

def mult(a, b, c): # описали функцию с 3-мя параметрами
	print(a*b*c)

def median(a, b): 
	return (a + b)/2 # return возвращает среднее арифметическое 2-х чисел

# numb_1 = 5
# numb_2 = 10
# numb_3 = 15
# mult(int(input('1:')), int(input('2:')), int(input('3:')))
# mult(numb_1, numb_2, numb_3)

numb_4 = median(3, 5)
print(numb_4 + 100)

# for i in range(100):
# 	summ()