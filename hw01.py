# Добавлена работа над ошибками

# 1. День недели.

# Можно добавить проверку коректности ввода.

# a = int(input("Введите день недели:"))
# if a == 6 or a == 7:
#     print("Выходной день.")
# else:
#     print("Рабочий день.")
    

# 2. Проверка истинности.

# Операторные скобки расставлены неверно
# Нужно перебрать все значения

# for x in [True,False]:
#     for y in [True,False]:
#         for z in [True,False]:
#             if not (x or y or z) == (not y and not y and not z):
#                 print("Верно!")   
#             else:
#                 print("Неверно.")
#                 break # работает некорректно
               
# else:
#     print("Все решения проверены.")


# 3. Определение четверти

# x = int(input("Введите X:"))
# y = int(input("Введите Y:"))

# if x == 0 and y == 0:
#     print("Начало координат.")
# elif x == 0:
#     print("Точка на оси У.")
# elif y == 0:
#     print("Точка на оси Х.")
# elif x > 0 and y > 0:
#     print("Четверть 1.")
# elif x < 0 and y > 0:
#     print("Четверть 2.")
# elif x < 0 and y < 0:
#     print("Четверть 3.")
# elif x > 0 and y < 0:
#     print("Четверть 4.")

# 4. Определение координат.

# a = int(input("Введите номер четверти (от 1 до 4):"))

# if a == 1:
#     print("x > 0, y > 0")
# elif a == 2:
#     print("x < 0, y > 0")
# elif a == 3:
#     print("x < 0, y < 0")
# elif a == 4:
#     print("x > 0, y < 0")
# else:
#     print("Неправильное число (от 1 до 4)")

# 5. Расстояние между точками.

# pAX = int(input("Введите координату X для точки A:"))
# pAY = int(input("Введите координату Y для точки A:"))
# pBX = int(input("Введите координату X для точки B:"))
# pBY = int(input("Введите координату Y для точки B:"))

# pointA = input("Введите х и у через пробел").split(" ")
# pointB = input("Введите х и у через пробел").split(" ")

# print(pointA)
# print(pointB)


# print(pow(pow(pBX-pAX,2)+pow(pBY-pAY,2),1/2))




# 6. Доп. задание. Кратно ли число 5 и 10 или 15, но не 30.

# if (n%5 == 0  and n%10 == 0) or n%15 == 0 and n%30 != 0 

# 7. Проверка корректности ввода.


# def enterInt():
#     while True:
#         try:
#             number = int(input("Введите целое число:"))
#             return number
#             # break
#         except:
#             print("Введите ЦЕЛОЕ число ещё раз.")

# numberOne = enterInt()
# print(numberOne)