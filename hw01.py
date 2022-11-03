# 1. Удаялем из текста

# subStr = 'абв'
# text = 'Привет мирабв! Кто здесь?'

# print('Вход:')
# print(text)

# spText = text.split()

# for i in range(len(spText)):
#     if spText[i].find(subStr) > 0:
#         spText[i] = ''

# print('Выход:')
# print(' '.join(spText).replace('  ',' '))


# 2. Игра с конфетами

# import random

# startBons = 15
# maxBons = 28
# players = ['Компьютер', 'Игрок']


# def inputBons(curBons: int):
#     inpBons = 0
#     while (inpBons < 1) or (inpBons > maxBons) or (inpBons > curBons) or (inpBons == ''):
#         try:
#             inpBons = int(input(f'Сколько взять конфет?: '))
#         except:
#             pass
#     return inpBons

# def chooseTurn(trn: int):
#     if trn%2 > 0:
#         return 1
#     else:
#         return 0

# def getBonsBot(bon: int):
#     if bon <= maxBons:
#         return bon
#     else:
#         inpBons = 1
#         while not (bon == inpBons + bon//maxBons*maxBons + 1) and (inpBons < maxBons):
#             inpBons += 1
#         return inpBons

# bonBons = startBons
# getBons = 0

# print('Бросаем жребий.')
# turn = random.randint(1,2)
# print(f'Начинает {players[chooseTurn(turn)]}.')
# print(f'На столе {bonBons} конфет.')


# while bonBons > 0:
#     print(f'Ход игрока: {players[chooseTurn(turn)]}')
#     if chooseTurn(turn) == 0:
#         getBons = getBonsBot(bonBons)
#     else:
#         getBons = inputBons(bonBons)
#     bonBons -= getBons
#     print(f'Игрок взял {getBons} конфет.')
#     print(f'Осталось {bonBons} конфет.')
#     turn += 1

# print(f'Победитель - {players[chooseTurn(turn-1)]}!')

# 4. RLE алгоритм

text1 = 'aaaaaaabbbbbbcccccccccd'
text2 = '11a3b7c1d'

def ToFile(file: str, strng: str):
    with open(file, 'w') as data:
        data.write(strng)


def FromFile(strng: str):
    with open(file, 'r') as data:
        return data.readline()


def compact(strng: str):
    strng = strng + ' '
    newStrng = ''
    while strng != ' ':
        pChar = strng[0]
        i = 1
        tempStr = ''
        while (pChar == strng[i]):
            i += 1
        tempStr = strng[:i]
        ni = tempStr.count(tempStr[0])
        newStrng += str(ni) + tempStr[0]
        strng = strng[i:]
    return newStrng

def decompress(strng: str):
    newStrng = ''
    newList = []
    i = 0
    while i < len(strng):
        if i > 0:
            if strng[i].isdigit != strng[i-1].isdigit:
                newStrng += ' '
        newStrng += strng[i]
        i += 1
    newList = newStrng.split()
    newStrng = ''
    for i in range(0, len(newList)-1, 2):
        newStrng += newList[i+1]*int(newList[i])
    return newStrng
        

file1 = 'textin.txt'
file2 = 'textout.txt'

myStr = text1
myStr = compact(myStr)
ToFile(file2, myStr)
myStr = decompress(myStr)
ToFile(file1, myStr)


