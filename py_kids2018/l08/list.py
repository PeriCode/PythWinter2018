my_list = ["Винни Пух","Гравити Фолз", "Лунтик", "Сказка о царе Солтане"]
# chaos_list = [1, 'Строка', True, None]
# print(chaos_list)

my_list[0] = "Карлсон, который живет на крыше"
# print(my_list)
my_list[1] = "Лоло и Пепе"
my_list.append("Галактический футбол") # добавление в конец
my_list.insert(2, "Пингвины Мадагаскара") # добавление на 2-ю позицию
my_list.extend(["Ежик в тумане", "Король лев"]) # слияние списков 

my_list.remove("Лунтик") # удаление из списка значения "Лунтик"
print(my_list)
del my_list[3] # удаляет третий элемент
print(my_list)

list_of_numb = [1, 4, 2, 7, 5]
print(list_of_numb)
list_of_numb.sort()
print(list_of_numb)