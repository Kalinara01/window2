'''Основные принципы ООП: Полиморфизм'''
'''Одинаковые название, разная работа'''
#pop
#list.pop()
# set.pop()
# dict.pop()

'''Полиморфизм - разное поведение одного и того же метода в разных класса'''

#1.примеры полиморфизма
#+
# [1,2,3] + [4,5,6] - получаем [1,2,3,4,5,6]
# 9 + 3 - получаем 12
# 'hello' + 'world' - получаем 'hello world'

# 2.
# len('Makers')
# len([1, 2, 'hello', 7])
# len([1: 'hello', 2: 'world'])
# ...

# 3.
#list.pop()
# set.pop()
# dict.pop()
'''один интерфейс - разный функционал'''

# class Cat:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age
#     def info(self):
#         print(f'It is a cat. Cats name is {self.name}, age {self.age}')
#     def make_sound(self):
#         print('Meow-meow')

# class Dog:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age
#     def info(self):
#         print(f'It is a gog. Dogss name is {self.name}, age {self.age}')
#     def make_sound(self):
#         print('Cav-cav')

# cat = Cat('Garfild', 5)
# dog = Dog('Pluto', 9)
# cat.make_sound()
# dog.make_sound()
# cat.info()
# dog.info()

# class Shape:
#     def __init__(self, name):
#         self.name = name
#     def area(self):
#         pass

# #     def fact(self):
#         return 'я фигура в двумерной плоскости'
    
#     def __str__(self):
#         return self.name
    
# class Square(Shape):
#     def __init__(self, length):
#         super().__init__('Square')
#         self.length = length

#     def area(self):
#         return self.length ** 2
    
#     def fact(self):
        # return 'У квадрата все стороны равны'

# from math import pi   
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__('Circle')
#         self.radius = radius

#     def area(self):
#         return pi * self.radius ** 2
    
    # def a(self):
    #     print('=====')
    
# for i in [Circle(4), Circle(9), Square(7)]:
#      print(i)
#      print(i.fact())
#      print(i.area())
    #  i.a()
    #  print('=====')


# class Phone:

#     __battery_level = 100
#     def __init__(self, imei, os):
#         self._imei = imei
#         self._oc = os

#     @property
#     def battery_level(self):
#         if self.__battery_level <= 0.5:
#             raise Exception('Телефон разряжает')
#         self.__battery_level -= 0.5

#     @property
#     def get_info(self):
#           if self.__battery_level <= 0.5:
#             raise Exception('Телефон разряжает')
#           self.__battery_level -= 0.5
#           print(self.__os, self.__imei)
#     def play_music(self):
#         if self.__battery_level <= 5:
#             self.__battery_level = 0
#             raise Exception('Телефон разряжен')
#         self.__battery_level -= 5
#         print('Слушаем Мирбекова Атабекова')

#     def play_video(self):
#         if self.__battery_level <= 7:
#             self.__battery_level = 0
#             raise Exception('Телефон разряжен')
#         self.__battery_level -= 5
#         print('Смотрим фильм')

#     def charge_battery(self, sec):
#         from datetime import datetime, timedelta

#         from time import sleep

#         now = datetime.now()

#         end_time = (now() + timedelta(seconds=sec)).strftime('%M:%S')

#         while now().strftime('%M:%S') != end_time:
#             sleep(1)
#             if self.__battery_level < 100:
#                 self.__battery_level += 1
#             print(f'Идет зарядка. Уровень батареи: {self.__battery_level}')

# phone = Phone('171-21-22-11', 'IOS 15')
# phone.battery_level
# phone.get_info

# phone.battery_level
# phone.play_music()
# phone.play_music()
# phone.play_music()
# phone.play_music()
# phone.play_music()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.charge_battery(10)
# # phone.play_video()
# phone.battery_level


# class Phone:

#     battery_level = 100

#     def __init__(self, imei, os):
#         # self.__battery_level = 100
#         self.__imei = imei
#         self.__os = os

#     @property
#     def battery_level(self):
#         if self.__battery_level <= 0.5:
#             raise Exception('Телефон разряжет')
#         self.__battery_level -= 0.5
#         print(self.__battery_level)

#     @property
#     def get_info(self):
#         if self.__battery_level <= 0.5:
#             raise Exception('Телефон разряжет')
#         self.__battery_level -= 0.5
#         print(self.__os, self.__imei)

#     def play_music(self):
#         if self.__battery_level <= 5:
#             self.__battery_level = 0
#             raise Exception('Телефон разряжен')
#         self.__battery_level -= 5
#         print('Слушаем Мирбека Атабекова')
    
#     def play_video(self):
#         if self.__battery_level <= 10:
#             self.__battery_level = 0
#             raise Exception('Телефон разряжен')
#         self.__battery_level -= 7
#         print('Смотрим Топлеса')

#     def charge_battery(self, sec):
#         from datetime import datetime, timedelta

#         from time import sleep

#         now = datetime.now

#         end_time = (now() + timedelta(seconds=sec)).strftime('%M:%S')


#         while now().strftime('%M:%S') != end_time:
#             sleep(1)
#             if self.__battery_level < 100:
#                 self.__battery_level += 1
#             print(f'Идет зарядка. Уровень батареи: {self.__battery_level}')

# phone = Phone('171-21-22-11', 'IOS 15')
# phone.battery_level
# phone.get_info

# phone.battery_level
# phone.play_music()
# phone.play_music()
# phone.play_music()
# phone.play_music()
# phone.play_music()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.charge_battery(10)
# # phone.play_video()
# phone.battery_level
