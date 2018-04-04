f = open('New file.txt', 'a')
f.write('Алоха\t')
f.close()

f = open('New file.txt')
text = f.readlines()
# for i in range(len(text)):
# 	text[i] = text[i].rstrip('\n')
print(text)
f.close()
