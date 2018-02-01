list_of_my_favourite_games = ["PUBG","CS_GO","Witcher"]
list_of_my_favourite_games.append("Dota")
list_of_my_favourite_games.insert(2,"Minecraft")
list_of_my_favourite_games.extend(["Warface","MAFIA"])
list_of_my_favourite_games.remove("CS_GO")
del list_of_my_favourite_games[1]
#print(list_of_my_favourite_games)

our_tuple = ("Защитники", "Движение вверх", "Легенда о Коловрате")
f1, f2, f3 = our_tuple
#print(f1, f2, f3)
books = {
	"Булгаков": ("Белая гвардия", "Собачье сердце", "Мастер и Маргоритта"),
	("Борис Стругацкий", "Аркадий Стругацкий"):("Обитаемый остров", "Пикник на обочине", "Трудно быть богом")

}
# print(books["Булгаков"])
books ["Чехов"] = ("Палата №6", "Вишневый сад")
print(books)

