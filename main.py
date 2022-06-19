#В доме живет N жильцов. Однажды решили провести перепись всех жильцов
 #данного дома и составили список, в котором указали возраст и пол каждого жильца.
 #Требуется найти номер самого старшего жителя мужского пола.
'''
dom = {25:1,23:0,55:1,30:0}
print(dom)
new_dom = list(dom)
print(new_dom)
a = max(dom)
print(a)
b = dom.get(a)
print(b)

list = (sorted(dom.items()))
x = len(list)
print(list)
for i in range(x-1,-1,-1):
    if list[i][1] == 1:
        age = list[i][0]
        break

n = 0
print("age",age)
for k in dom.keys():
    if k != age:
        n=n+1
print(n)
'''
# Задача с конфетами
import random


konfeti = 100
max = 28

while konfeti>=28:
#Я ввожу количество конфет
 print("Введите количество конфет,которое вы берете,но не более 28: ")
 a = int(input())
 konfeti = konfeti - a

#Ход для бота(интеллектуальный выбор: если рандомное число четное,
# то высчитывает свой ход по формуле,если нет - берет другое рандомное число
 c = 0
 b = random.randint(1,10)

 print(b)

 if b % 2 == 0:
    c = konfeti % (max + 1)
    print("Проверка,бот взял: ", c)
 if b % 2 == 1:
    c = random.randint(1,28)

 if konfeti <= 28:
    c = konfeti
 konfeti = konfeti - c
 print("Бот взял: ", c)
 print(" Осталось",konfeti,"конфет")

# Проверки
print(konfeti)
if 1 <= konfeti < 28:
 print("Вы выиграли!")
if konfeti == 0:
 print("Вы проиграли...")
