# # hw2. задание 3. Последовательность (1+1/n)^n


# def fillRow(number):
#     # myOrder = []
#     # for i in range(number):
#     #     myOrder.append(pow(1+1/(i+1), i+1))
#     # return myOrder
#     return list(map(lambda x: pow(1+1/(x+1), x+1), [x for x in range(number)]))
    

# def sumRow(strRow):
#     res = 0
#     for i in range(len(strRow)):
#         res += strRow[i]
#     return res

# a = int(input("Введите число:"))
# myRow = fillRow(a)
# print(f'Последовательность:\n{myRow}')
# print(f'Сумма последовательности:\n{sumRow(myRow)}')


# #HW3. Задание 1. Сумма нечетных элементов

# import random

# # numbers = ['2','3','5','9','3']
# numbers = [random.randint(1,9) for _ in range(10)]

# summ = 0
# for i in range(1,len(numbers),2):
#     summ += int(numbers[i])
# print(f'Исходные числа:{numbers}')
# print(f'Сумма нечетных элементов: {summ}')