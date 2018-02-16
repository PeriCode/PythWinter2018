def faktor(a):
	if a == 0:
		return 1
	else:
		return a * faktor(a - 1)