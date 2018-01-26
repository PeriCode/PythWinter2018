our_str = "hello \"world\"" # \ - экранирование
our_str_2 = "Veni, vidi, vici!"

# print(our_str)
# our_str[0] = 'H' # Так нельзя, 
# str - неизменяемый тип

print(our_str_2[12:17])
print(our_str_2[12:]) # от 12-го символа до конца
print(our_str_2[:10]) # от самого начала до 10-го символа
print(our_str_2[-1]) # последний символ
print(our_str_2[-3:]) # срез, отсчет конца
print(our_str_2[:]) # вывод всей строки
print(our_str_2[7:3]) # жаль
print(our_str_2[-1:-3]) # снова жаль
print(our_str_2[1::2]) # вывод каждого второго символа
print(our_str_2[::-1]) # вывод в обратном порядке

Favourite_Saeeds_text = """Lorem ipsum dolor sit amet,
consectetur adipisicing elit, sed do eiusmodtempor incididunt 
ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
commodo consequat. Duis aute irure dolor in reprehenderit in 
voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur int occaecat cupidatat non proident, sunt in culpa 
qui officia deserunt mollit anim id est laborum."""

#print(Favourite_Saeeds_text.lower()) # все символы в нижний регистр
#print(Favourite_Saeeds_text.upper()) # все символы в верхний регистр
print("\nгде мой биткоин?".upper())
#print(Favourite_Saeeds_text.title())
#print(Favourite_Saeeds_text.replace(' ', '')) # замена
print(Favourite_Saeeds_text.find("dolor")) 
print(Favourite_Saeeds_text.rfind("dolor")) 
print(len(Favourite_Saeeds_text)) # количество символов
print(Favourite_Saeeds_text.count("dolor")) # количество вхождения строки dolor

