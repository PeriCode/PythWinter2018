my_str = "Merry Christmas"

print(my_str[6])
# my_str[0] = 'm' # str - неизменяемый тип
print(my_str[6:11]) # срез строки
print(my_str[6:]) # срез от 6-го и до конца
print(my_str[:5]) # срез от начала до 5-го символа
# конец не включен
print(my_str[:]) # срез всей строки 
print(my_str[-1]) # последний символ
print(my_str[-3:]) # последние 3 символа
print(my_str[1::2]) # меняем шаг среза
print(my_str[::-1]) # срез-инверсия слова
print(my_str[1:1000]) # штрафа за превышение нет

fish_text ="""Lorem ipsum dolor sit amet, 
consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation 
ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit 
anim id est laborum."""

print(len(fish_text)) # длина строки
# print(fish_text.lower()) # все символы к нижнему регистру
# print(fish_text.upper()) # наоборот
# print(fish_text.title())

# print(fish_text.replace(" ","")) # заменяем часть строки
# print(fish_text.find("dolor"))
# print(fish_text.rfind("dolor"))
# print(fish_text.count("."))
norm_text = "123456789"
# print(norm_text[:len(norm_text)//2+1]) # берем срез по половине текста
print(norm_text[len(norm_text)//2 + 1:][::-1] + norm_text[:len(norm_text)//2+1])
