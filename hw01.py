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

def ToFile(strng: str):
    print(strng)

def FromFile(strng: str):
    return strng

def compact(strng: str):
    newStrng = []
    for i in range(len(strng)):
        newStrng.append(strng[i])
    # for i in newStrng:
    #     if i.index()+1 <= len(newStrng):
    #         if (i != newStrng[i.index()+1]):
    #             newStrng.insert(i.index(),' ')

    
    # i = 0
    # while i < len(newStrng):
    #     i += 1
    #     if (newStrng[i] != newStrng[i-1]) and (newStrng[i-1] != ' '):
    #         newStrng.insert(i,' ')
    #         print(newStrng)
            
    # Фрагмент ниже выдает неожиданные данные. Хотя и сам цикл не идеален            
    # ni = ''
    # counti = 0
    # for i in range(len(strng)):
    #     print(i, strng[i], newStrng)
    #     if (strng[i] != ni) and (counti != 0):
    #         newStrng += str(counti) + ni
    #         counti = 0
    #         ni = strng[i]
    #         # print(newStrng)
    #     counti += 1
    return newStrng

myStr = FromFile(text1)
myStr = compact(myStr)
ToFile(myStr)


