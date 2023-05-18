# data = (4, 6, 7, 3, 6, True, 5.6,'Hello')
# print(data[1:5])

# print(data.count(6))
# print(len(data))

# data = (4, 6, 7, 3, 6, True, 5.6,'Hello')
# for el in data:
#     print(el)

#     nums = [5,7,8]

#     new_data = tuple(nums)
#     word = tuple('Hello World')
#     print(word)

# country = {'code': 'Ru', 'name':'Russian','population':144}
# print(country['population'])
# print(country)
# for key,value in country.items():
#     print(key, '-',value)

# person = {'user-1':{
#     'first_name':'Join',
#     'last_name':'Marley',
#     'age':45,
#     'adress':['г.Москва.'],
#     'grades':{'math':5,'physics':3}
# }
          
# }
# print(person['user-1']['first_name']['adress'])

# data = set ('hello')
# data = {5, 7, 5, 6, 7, 8}
# data.add(32)
# data.update(['32',True,4,6])
# data.remove('32')
# data.remove(True)
# data.pop()
# data.clear()
# nums = [5, 4, 2, 7, 9, 7]
# new_nums = set(nums)
# data_new = frozenset(['32',True,4, 6, 5, 7, 5, 6, 7, 8,5, 4, 2, 7, 9, 7 ])
# print(data_new)

# def text_func(word):
#     print(word, end='')
#     print('!')


# text_func('hi')
# text_func(2)
# text_func(3)

# def summa(a, b):
#     return  a + b
    
# res = summa(5, 7)
# print(res)
  
# def minimal(l):
#     min_number = l[0]
#     for el in l:
#      if el < min_number:
#         min_number = el
#     return min_number

# nums1 = [12, 8, 9,54, 0.1,6,0.2, 2.3]
# min1 = minimal(nums1)
# nums2 = [5, 7, 6, 8, 2.1, 6.2, 0.2]
# min2 = minimal(nums2)
# if min1< min2:
#   print(min1)
# else:
#   print(min2)

# funs = lambda x, y: x * y 
# res = funs(5, 2)
# print(res)



# 


# try:
#     x = int(input('Введите число: '))
#     x+= 5
#     print(x)
# except ValueError:
#     print('Введите лучше число') 


# x = 0
# while x == 0:
#     try:
#         x = int(input('Введите число: '))
#         x *= 5
#         print(x)
#     except ValueError:
#         print('Введите лучше число') 


# try:
#    with open('text.txt', 'r', encoding='utf-8') as file:
#        print(file.read())
# except FileNotFoundError:
#     print('Файл не найдет')

import datetime as d, sys,os,platform
from math import sqrt

# # print(d.datetime.now().date())
# print(platform.system())
print(sqrt(1023 ))
