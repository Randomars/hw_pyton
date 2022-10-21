# 1. Сумма цифр вещественного числа

# numbers = ('0','1','2','3','4','5','6','7','8','9')

# a = str(input("Введите вещественное число:"))
# summ = 0
# for i in a:
#     if i in numbers:
#         summ = summ + int(i)
# print(f'Сумма цифр числа: {summ}')


# 2. Произведения  N

# Вариант 1.

# a = int(input("Введите число:"))

# produkt = []
# for i in range(a):
#     bitProd = 1
#     for j in range(i):
#         bitProd *= j+2
#     produkt.append(bitProd)
# print(f'Произведение чисел до N: {produkt}')


# Вариант 2.

# a = int(input("Введите число:"))

# strProdukt = []
# for i in range(a):
#     bitProd = '1'
#     for j in range(i):
#         bitProd = bitProd + '*' + str(j+2)
#     strProdukt.append(bitProd)
# print(f'Набор произведений числа N: {strProdukt}')


# 3. Последовательность (1+1/n)^n


# def fillRow(number):
#     myOrder = []
#     for i in range(number):
#         myOrder.append(pow(1+1/(i+1), i+1))
#     return myOrder

# def sumRow(strRow):
#     res = 0
#     for i in range(len(strRow)):
#         res += strRow[i]
#     return res

# a = int(input("Введите число:"))
# myRow = fillRow(a)
# print(f'Последовательность:\n{myRow}')
# print(f'Сумма последовательности:\n{sumRow(myRow)}')


# 4. Перемешивание списка

from random import randint


listOne = ['1', '2', '3', '4']

listTwo = listOne

print(listTwo)
for i in range(10):
    a = randint(0,len(listTwo)-1)
    b = randint(0,len(listTwo)-1)
    temp = listTwo[a]
    listTwo[a] = listTwo[b]
    listTwo[b] = temp
print(listTwo)


