list_of_films = ['Движение вверх', 'Дивергент', 'Джуманджи']
list_of_numbs = [1, 4, 7, 10, 5, 2]

list_of_films.append('Трансформеры')
list_of_films[1] = 'Время первых'
list_of_films.insert(2, 'Легенда №17')

del list_of_films[3]
list_of_films.remove('Трансформеры') 
print(list_of_films)