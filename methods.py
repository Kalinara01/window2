'''Методы экземпляра, класса, статические'''
# 1. методы экземпляра или объекта - isinstance methods
# 2. методы класса - class methods
# 3. статические методы - static methods

'''isinstance methods - обычные методы, которые принимают первым аргументом self. нужны для работы с атрибутами объекта'''

# class A:

#     def isinstance_methods(self):
#         print('методы экземпляра')

# a = A()
# # a.isinstance_methods()
# A.isinstance_methods(a)

'''методы класса -  class methods
первым аргументом принимают ссылку на класс, cls.Нужны для создания объектов или изменения атрибутов класса. 
Для создания используют декоратор @classmethods
 '''

# class B:

#     @classmethod
#     def class_methods(cls):
#         print('метод класса')
#         print('метод аргумент:', cls)

# b = B()
# b.class_methods()

# class Car:
#     color ='red'

#     @classmethod
#     def change_color(cls, value):
#         print(cls)
#         cls.color = value

'''Методы класса меняют состояние всего класса, и это отражается на оюъектах созданных от этого классаю 
Не могут менять состояние конткретного объекта (это делают методы объекта)'''

# print(Car.color)
# Car.change_color('black')

# print(Car.color)

# class Pizza:

#     def __init__(self, radius, *ingredients):
#         self.radius = radius
#         self.ingred = ingredients

#     def cook(self):
#         print(f'готовится пицца размером {self.radius * 2} см')
#         print(f'Ингридиенты: {self.ingred}')

#     @classmethod
#     def four_cheeze(cls, r):
#         pizza = cls(r,'Моцарелла', 'Чеддер', 'Голландский', 'Дор блю')
#         return pizza

# pizza = Pizza(15, 'Моцарелла', 'Чеддер', 'Голландский', 'Дор блю')

# p = Pizza.four_cheeze(15)
# p.cook()
# p1 = Pizza.four_cheeze(20)
# p1.cook()


'''Статические методы - Static methods
создается при помощи декоратора @staticmethod, не принимает ссылку ни на класс, ни на объект.
Просто функция внутри класса, которая ничего не знает о объекте, и о классе.
Используется внутри класса(вспомогательные функции) - изменение типа данных, расчеты и т.д
'''

# class C:

#     @staticmethod
#     def hello():
#         print('hello')

# object = C()
# object.hello()
# C.hello()

# class Cylinder:
#     def __init__(self, diametr, hight) -> None:
#         self.di = diametr
#         self.hi = hight
#         self.area = self.get_area(diametr, hight)

#     @staticmethod
#     def get_area(di, hi):
#         from math import pi
#         circle = pi * di ** 2 / 4
#         side = pi * di * hi
#         area = circle * 2 + side
#         return area
    
# # c = Cylinder(12, 5)   
# # print(c.area)

# print(Cylinder.get_area(4, 6))


# class Home:
#     count_people = 0

#     def __init__(self, name, people, last_name) -> None:
#         self.name = name
#         self.people = people
#         self.last_name = last_name
#         Home.count_people += people

#     def info(self):
#         print(self.name, self.last_name)

#     @classmethod
#     def people(cls):
#         print(cls.count_people)

#     @staticmethod
#     def about_home():
#         print('4 этажа, 26 квартир')

# a = Home('Sam', 4, 'last_name')
# print(a.count_people)
# b = Home('gg', 8, 'kk')
# print(a.count_people)
# a.people
# b.about_home()


# class Iphone:
#     cost = 100000

#     def __init__(self, name, money):
#         if money < Iphone.cost:
#             raise Exception('У вас не хватило денег на покупку')
#         self.name = name
    
#     @staticmethod
#     def about_phone():
#         print('starage: 256\color: purple')

#     @classmethod
#     def change_cost(cls, new_cost):
#         cls.cost = new_cost
#         print(f'Новая стоимость:{new_cost}')


# a = Iphone('Jonh', 100000)
# print(a.cost)
# a.change_cost(90000)
# print(a.cost)

# class A:

#     def a(self, b):
#         self.b = b

# a = A()
# A.a(a, 5)
# print(a.__dict__)
# A.a(a.__class__, 9)
    


    


    





 