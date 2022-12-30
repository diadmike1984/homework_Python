
# № 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# def Method (number: int) -> list:
#     number = abs(number)
#     i = 2
#     factors = []

#     while i * i <= number:
#         if number % i:
#             i += 1

#         else:
#             number //= i
#             factors.append(i)

#     if number > 1:
#         factors.append(number)

#     return factors

# number_to_decompose = int(input('Enter a number to decompose: '))
# number_farctors = Method(number_to_decompose)
# print('Decomposed number:')
# print(number_to_decompose, '=', ' * '.join(map(str, number_farctors)))

# № 2. Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, сколько указал пользователь(БЕЗ round())


# from math import pi

# fraser = str(pi)

# length_of_pi = []

# number_of_places = int(input("Enter the number of decimal places you want: "))

# for places in range(number_of_places + 2):
#     length_of_pi.append(str(fraser[places]))

# print("".join(length_of_pi))

# № 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")


# № 4.  Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.

# from random import randint
# max_val = 100
# k = int(input('Введите натуральную степень k:'))
# koeff=[randint(0,max_val) for i in range(k)]+[randint(1,max_val)]
# poly='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koeff) if j][::-1])
# poly=poly.replace('x^1+', 'x+')
# poly=poly.replace('x^0', '')
# poly+=('','1')[poly[-1]=='+']
# poly=(poly, poly[:-2])[poly[-2:]=='^1']
# print(poly)