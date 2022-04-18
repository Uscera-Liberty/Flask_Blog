# def is_palidrom(in_str):
#     """Return True if string reads from the beginning the same form the end"""
#     return in_str == in_str[::-1]
# print(is_palidrom('salas'))
# print(is_palidrom('anna'))
# print(is_palidrom('more'))
# # dry = don't repeat yourself
#
#
#
# def opitimized_is_palidrom(in_str):
#     arr_len =len(in_str)
#     for index in range(arr_len // 2):
#         if in_str[index] != in_str[- 1 - index]:
#             return False
#     return True
# #
# #
# """отсортированный массив: функция принимает некоторый массив и некоторое число :
# возвращает 2 значения из массива которые в сумме дают таргет"""
#
# def binary_search(lys, val):
#     first = 0
#     last = len(lys)-1
#     index = -1
#     while (first <= last) and (index == -1):
#         mid = (first+last)//2
#         if lys[mid] == val:
#             index = mid
#         else:
#             if val<lys[mid]:
#                 last = mid -1
#             else:
#                 first = mid +1
#     return index
#
# def sort_mas(list , target):
#     a = []
#     temp = []
#     for i in range(len(sorted(list))):
#         ost = target - list[i]
#         if ost in list:
#             index = binary_search(list,ost)
#             a.append([list[i], list[index]])
#         elif ost not in list:
#             pass
#
#     for x in range(len(a) - 1):
#         if a[x][0] != a[x + 1][0]:
#             temp.append(x)
#     return a , temp
#
# n , target = map(int , input().split())
# list = [int(i) for i in input().split()]
# print(sort_mas(sorted(list), target))

# print(sort_mas([-6 ,-5 , 0 , 2 , 3 , 5] , 18))
# print(sort_mas([0, 1, 2, 3, 4, 5, 6, 7, 8, 9] , 17))

# 7 7
# 4 3 4 8 4 3 4

# Массив делится пополам — на левую и правую половины.
# Элементы разбиваются на группы.
# На первой итерации это двойки элементов (1-й элемент левой половины + 1-й элемент правой половины, 2-й элемент левой половины + 2-й элемент правой половины и т.д.), на второй итерации — четвёрки элементов (1-й и 2-й элементы левой половины + 1-й и 2-й элементы правой половины, 3-й и 4-й элементы левой половины + 3-й и 4-й элементы правой половины и т.д.), на третьей — восьмёрки и т.д.
# Элементы каждой группы из левой половины являются отсортированным подмассивом, элементы каждой группы из правой половины также являются отсортированным подмассивом.
# Производим слияние отсортированных подмассивов из предыдущего пункта.
# Возвращаемся в п


n = int(input())
n_eli = 1
c = 0
while n > n_eli :
    n = n - n_eli
    n_eli += 1
    c+= 1
print(c)