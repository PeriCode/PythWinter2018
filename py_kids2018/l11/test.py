txt = input("Введите температуру через пробел").split(' ')
print(txt)
s = 0
for i in txt:
	s += int(i)

print(s/len(txt))