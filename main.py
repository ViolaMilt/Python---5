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
''' 
# 2. Создайте программу для игры в "Крестики-нолики".
import pprint
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

A[0][0] == 1, A[0][1] == 2, A[0][2] == 3
A[1][0] == 4, A[1][1] == 5, A[1][2] == 6

for i in range(len(A)):
     for j in range(len(A[i])):
         print(A[i][j], end=' ')
     print()
     z = [1, 2, 3, 4, 5, 6, 7, 8, 9]


pobeda = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8],
         [0, 3, 6],
         [1, 4, 7],
         [2, 5, 8],
         [0, 4, 8],
         [2, 4, 6]]

win = ""

 # Основная программа
okonchanie = False
igra = True

while okonchanie == False:
    print('Введите число,соответствующее месту,куда вы хотите сделать ход')
    s = int(input())

    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == s:
                A[i][j] = "O"
            print(A[i][j], end=' ')
        print()

    for k in range(0,3):
        if A[k][0] == "X" and A[k][1] == "X" and A[k][2] == "X":
            win = "X"
        if A[k][0] == "O" and A[k][1] == "O" and A[k][2] == "O":
            win = "O"
        if A[0][0] == "X" and A[1][1] == "X" and A[2][2] == "X":
            win = "X"
        if A[0][0] == "O" and A[1][1] == "O" and A[2][2] == "O":
            win = "O"

        if A[0][2] == "X" and A[1][1] == "X" and A[2][0] == "X":
            win = "X"
        if A[0][2] == "O" and A[1][1] == "O" and A[2][0] == "O":
            win = "O"

    if win != "":
        # game_over = True
        print("Победил", win)
        break
    if win == "":
        game_over = False


        symbol = "O"
        step = int(input("Ход 2 игрока: "))
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == step:
                    A[i][j] = "X"
                print(A[i][j], end=' ')
            print()
        for k in range(0,3):
            if A[k][0] == "X" and A[k][1] == "X" and A[k][2] == "X":
                win = "X"
            if A[k][0] == "O" and A[k][1] == "O" and A[k][2] == "O":
                win = "O"
    if win != "":
        game_over = True
        print("Победил", win)
        break
    if win == "":
        game_over = False



