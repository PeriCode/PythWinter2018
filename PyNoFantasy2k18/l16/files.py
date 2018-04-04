f = open('Новый файл.txt', 'w')
f.write('Привет, мир!\n')
f.write('Саид пишет стихи')
f.close()

f = open('Новый файл.txt')
print(f.read(10))
f.close()