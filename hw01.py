# Привет, Стоун!
# Язык питон такой легкий, что на нем надо писать совсем не так как на освоенном C#. 
# Спасибо за подсказку, что новое задание надо делать с использованием словарей. 
# У меня сразу появились идеи для решения, а то на примере прошлого ДЗ для Фибоначчи я брал идею из варината на C#.
# А после обсуждения на семинаре, у меня получилось вот такое элегантное решение (там только формальный косяк при индексе 0):

# a = int(input("Введите значение индекса: "))
# rF = [1, 0, 1]

# for _ in range(2, a + 1):
#     rF.append(rF[len(rF)-1] + rF[len(rF)-2])
#     rF.insert(0, rF[1] - rF[0])

# print(rF)

# Вобще, после лекции, непонятна область применения всех этих вариантов списков (кортежей, множеств и тд), 
# и в голову идут "стандартные" решения C#, а тут надо делать изящнее, по питоновски.
# Спасибо за проверку работ:). А теперь новое ДЗ.

# P.S. Ой что-то я умаялся с выполнением. Поду смотреть решения.



# 1. Число ПИ

# import math

# a = float(input("Введите точность числа ПИ (в формате 0.001): "))
# if a == 0:
#     exit()

# i = 0
# while a < 1:
#     i += 1
#     a *= 10
# print(round(math.pi, i))


# 2. Простые множители числа.

# Вариант 1.

# a = int(input("Введите число: "))
# N = a

# print('Строим ряд простых чисел')
# simplList = [2]

# for i in range(3, a//2+1, 2):
#     mark = True
#     for j in simplList:
#         if i % j == 0:
#             mark = False
#     if mark == True:
#         simplList.append(i)

# print('Выбираем множители заданного числа')
# numSimpleList = []

# while a > 1:
#     for i in simplList:
#         if a % i == 0:
#             numSimpleList.append(i)
#             a = int(a / i)

# print(f'Список простых множителей числа {N}:')
# print(numSimpleList)

# Вариант 2. Оказалось всё проще.

# a = int(input("Введите число: "))
# N = a

# numSimpleList = []
# i = 2

# while a > 1:
#     while a % i == 0:
#         a = a // i
#         numSimpleList.append(i)
#     i += 1

# print(f'Список простых множителей числа {N}:')
# print(numSimpleList)


# 3. Список неповторяющихся элементов последовательности

# from random import randint as rnd

# l = rnd(10,20)
# row0 = []

# for _ in range(l):
#     row0.append(rnd(0,9))

# strInput = ''
# for i in range(len(row0)):
#     strInput += str(row0[i])

# rowStart = []
# rowEnd = []
# for i in strInput:
#     if i not in rowStart:
#         rowEnd.append(i)
#     elif len(rowEnd) > 0:
#         j = 0
#         while j < len(rowEnd):
#             if rowEnd[j] == i:
#                 rowEnd.pop(j)
#             j += 1
#     rowStart.append(i)

# print('В последовательности:')
# print(strInput)
# print('Неповторяющиеся элементы:')
# print(rowEnd)

# 4. Запись многочлена степени k.

# from random import randint as rnd

# k = int(input("Введите степень многочлена: "))

# koefRange = 100
# mnogochlenD = {}
# mnogochlenStr = ''
# mnogochlenD[k] = 0

# while mnogochlenD[k] == 0:
#     mnogochlenD[k] = rnd(-koefRange,koefRange)

# for i in range(k):
#     koef = rnd(-koefRange,koefRange)
#     if koef != 0:
#         mnogochlenD[i] = koef

# for i in range(k,-1,-1):
#     if i in mnogochlenD:
#         if i == k:
#             mnogochlenStr = str(mnogochlenD[i])
#         elif mnogochlenD[i] > 0:
#             mnogochlenStr = mnogochlenStr + ' + ' + str(mnogochlenD[i])
#         elif  mnogochlenD[i] < 0:
#             mnogochlenStr = mnogochlenStr + ' - ' + str(abs(mnogochlenD[i]))
    
#         if i == 1:
#             mnogochlenStr = mnogochlenStr + '*x'
#         elif i != 0:
#             mnogochlenStr = mnogochlenStr + '*x**' + str(i)
# else:
#     mnogochlenStr = mnogochlenStr + ' = 0'

# print(f'Многочлен: {mnogochlenStr}')

# path = r'text.txt'

# with open(path, 'w', encoding='UTF-8') as data:
#     data.write(mnogochlenStr)
# print(f'Сохнанен в файл "{path}"')


# 5. Сложение 2х многочленов

# path1 = r'text1.txt'
# path2 = r'text2.txt'
# path3 = r'solution.txt'


# def ToDict(textIn: str):
#     mnogoD = {}
#     for i in textIn:
#         if i.find('*x**') > 0:
#             dataBit = i.split('*x**')
#             mnogoD[int(dataBit[1])] = int(dataBit[0])
#         elif i.find('*x') > 0:
#             mnogoD[1] = int(i.replace('*x', ''))
#         else:
#             mnogoD[0] = int(i)
#     return mnogoD


# with open(path1, 'r', encoding='UTF-8') as data:
#     file1 = data.readline()
# mnogoD1 = ToDict(file1.replace(' = 0', '').replace(' + ', ' ').replace(' - ', ' -').split())
    
# with open(path2, 'r', encoding='UTF-8') as data:
#     file2 = data.readline()
# mnogoD2 = ToDict(file2.replace(' = 0', '').replace(' + ', ' ').replace(' - ', ' -').split())

# mnogoD3 = {}
# for i in mnogoD1:
#     mnogoD3[i] = mnogoD1[i] + mnogoD2[i]


# for i in mnogoD3.keys():
#     k = i

# for i in mnogoD3.keys():
#     if k < i:
#         k = i

# mnogochlenStr = ''

# for i in range(k,-1,-1):
#     if i in mnogoD3:
#         if i == k:
#             mnogochlenStr = str(mnogoD3[i])
#         elif mnogoD3[i] > 0:
#             mnogochlenStr = mnogochlenStr + ' + ' + str(mnogoD3[i])
#         elif  mnogoD3[i] < 0:
#             mnogochlenStr = mnogochlenStr + ' - ' + str(abs(mnogoD3[i]))
    
#         if i == 1:
#             mnogochlenStr = mnogochlenStr + '*x'
#         elif i != 0:
#             mnogochlenStr = mnogochlenStr + '*x**' + str(i)
# else:
#     mnogochlenStr = mnogochlenStr + ' = 0'

# print('Сумма многочленов:')
# print(file1)
# print(file2)
# print('Получена в виде:')
# print(mnogochlenStr)

# with open(path3, 'w', encoding='UTF-8') as data:
#     data.write(mnogochlenStr)
# print(f'Результат сохнанен в файл "{path3}"')

