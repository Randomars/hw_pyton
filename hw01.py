# 1. Сумма нечетных элементов

# numbers = ['2','3','5','9','3']

# summ = 0
# for i in range(1,len(numbers),2):
#     summ += int(numbers[i])
# print(f'Исходные числа:{numbers}')
# print(f'Сумма нечетных элементов: {summ}')


# 2. Произведения  пар

# numbers = ['2','3','4','5','6']

# i = 0
# produkt = []

# while i < len(numbers)/2:
#     produkt.append(int(numbers[i])*int(numbers[len(numbers)-i-1]))
#     i += 1
# print(f'Исходные числа:{numbers}')
# print(f'Произведение пар чисел: {produkt}')


# 3. Разница дробных частей

# numbers = [1.1, 1.2, 3.1, 5, 10.01]

# minFrac:float = 0
# maxFrac:float = 0

# for i in numbers:
#     if i % 1 > 0:
#         minFrac = i % 1
#         maxFrac = i % 1
#         break

# for i in numbers:
#     if i % 1 > 0:
#         if i % 1 < minFrac:
#             minFrac = i % 1
#         if i % 1 > maxFrac:
#             maxFrac = i % 1

# print(f'Исходные числа:{numbers}')
# print(f'Разница между значениями дробных частей: {maxFrac - minFrac}')


# 4. Преобразование в двоичное число.

# a = int(input("Введите число: "))
# binaryRes = ''

# while a / 2 > 0:
#     if a%2 == 0:
#         binaryRes = '0' + binaryRes
#     else:
#         binaryRes = '1' + binaryRes
#     a = int(a/2)

# print('Это число в двоичной системе: ' + binaryRes)


# 5. Список чисел Фибоначчи

def Fibonacci(n: int):
    if (n == 1) or (n == 2):
        return 1
    else:
        if n > 0:
            return Fibonacci(n - 1) + Fibonacci(n - 2)
        else:
            return Fibonacci(n + 2) - Fibonacci(n + 1)

a = int(input("Введите значение индекса: "))
rowFibonacci = []
for i in range(-a,a+1):
    rowFibonacci.append(Fibonacci(i))

print(rowFibonacci)

