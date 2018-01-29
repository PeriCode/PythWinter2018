# my_list = [] # объявили пустой список 
# # print(list('строка')) # преобразовали строку в список

# my_list = [1, 2, 3] # список из чисел
# print(my_list[0:2]) # срез списка 
# my_list[2] = '3' 
# my_list[1] = [1.5, 2.5]
# print(my_list)
# print(my_list[1][0]) # двойная индексация

worlds = ['Warhammer','the Lord of the Rings','DC']
worlds.append('Vampire the Maquerade')
worlds.insert(0, 'Мечты Навального')
anime_worlds = ['Ну, погоди!', 'Наруто', 'Призрак в доспехах']
# worlds.append(anime_worlds)
# worlds += anime_worlds
worlds.extend(anime_worlds)
worlds.append('Призрак в доспехах')
worlds.remove('Призрак в доспехах') # удаляет по значению 
del worlds[-2] # удаляет по индексу
bred = worlds.pop(0) # удаление с возвратом

worlds_copy = worlds[:]

worlds_copy.append('Ведьмак')
print(worlds)
print(worlds_copy)

list_of_numbers = [3, 6, 1, 7, 4, 2, 2, 4, 10]
print(list_of_numbers.sort())
print(max(list_of_numbers)) # возвращает макс эл
print(min(list_of_numbers)) # возвращает мин эл
print(len(list_of_numbers))
