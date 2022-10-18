# 1. День недели.

# a = int(input("Введите день недели:"))
# if a == 6 or a == 7:
#     print("Выходной день.")
# else:
#     print("Рабочий день.")
    

# 2. Проверка истинности.

# myArray = []

# for i in range(3):
#     myArray.append(bool(input(f"Введите значение {i+1}:")))
# print(myArray)
# if not (myArray[0] or  myArray[1] or myArray[2]) ==  (not myArray[0]) and (not myArray[1]) and (not myArray[2]):
#     print("Верно!")   
# else:
#     print("Неверно.")


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

pAX = int(input("Введите координату X для точки A:"))
pAY = int(input("Введите координату Y для точки A:"))
pBX = int(input("Введите координату X для точки B:"))
pBY = int(input("Введите координату Y для точки B:"))

print(pow(pow(pBX-pAX,2)+pow(pBY-pAY,2),1/2))
    