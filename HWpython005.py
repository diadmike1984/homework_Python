# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

# 120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф

# from random import randint


# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


# def bot_calc(value):
#     k = randint(1, 29)
#     while value-k <= 28 and value > 29:
#         k = randint(1, 29)
#     return k


# player1 = input("Введите имя первого игрока: ")
# player2 = "Bot"
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0, 2)
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = bot_calc(value)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")



# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"

# stroka = "3a4b2c3b"

# Вывод: stroka = "aaabbbbccbbb"


# with open('RLE.txt', 'w', encoding='UTF-8') as file:
#     file.write(input('Напишите текст необходимый для сжатия: '))
# with open('RLE.txt', 'r') as file:
#     text = file.readline()
#     text_compress = str(text)

# def rle_encode(data):
#     encoding = ''
#     prev_char = ''
#     count = 1

#     if not data: return ''

#     for char in data:

#         if char != prev_char:
#             if prev_char:
#                 encoding += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     else:
#         encoding += str(count) + prev_char
#         return encoding

# encoded_val = rle_encode(text_compress)
# print(f'Информация в сжатом виде: {encoded_val}')

# with open('RLE1.txt', 'w', encoding='UTF-8') as file:
#     file.write(encoded_val)
# with open('RLE1.txt', 'r') as file:
#     text1 = file.readline()
#     text_decompress = str(text1)

# def rle_decode(data):
#     decode = ''
#     count = ''
#     for char in data:
#         if char.isdigit():
#             count += char
#         else:
#             decode += char * int(count)
#             count = ''
#     return decode

# decoded_val = rle_decode(text_decompress)
# print(f'А вот и декодированная информация: {decoded_val}')