# import random

text = input("Введи текст: ")
# print(text.replace('a', '1 ').replace('b', '2 ')
# .replace('c', '3 ').replace('d','4 '))
print(text[:len(text) // 2])
print(text[len(text) // 2:])
print(text[len(text) // 2:] + text[:len(text) // 2])