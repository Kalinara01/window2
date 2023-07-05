'''Магические методы в Python (dunner - double underscore)'''

'''методы у которых 2 нижних подчеркивания в начале и 2 в конце, 
мы их не вызываем напрямую, они вызываются определенным операторами или функция'''

#__init__, __str__

#__new__() - конструктор, отвечает за создание объекта
#__init__() - инициализатор, задает созданному объекту атрибуты
#__del__() - деструктор, отвечает за удаление объекта

# class Point:

#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y
#     def __del__(self):
#         print('удаление экземпляра' + str(self))
# a = Point(0, 4)


# class Point:
#     def __new__(cls, *args, **kwargs):
#         print('Вызываетсяметод __new__' + str(cls))
#         return super().__new__(cls)
    
#     def __init__(self, x, y) -> None:
#         print('вызов метода __init__' + str(self))
#         self.x = x
#         self.y = y

# a = Point(1, 2)

# class Word(str):

#     def __new__(cls, *args):
#         string = args[0].replace('', '')
#         return str.__new__(cls, string)
    
# a = Word('ddsdsfadazc tagfz afdcx dsx')
# print(a)

# class User:

#     def __new__(cls, name, age):
#         if age > 18:
#            raise ValueError('Выслишком молоды')
#         else:
#             return super().__new__(cls)

#     def __init__(self, name, age):
#         print('init')
#         self.name = name
#         self.age = age

#     def __del__(self):
#         print('Пока')
'''для чтения'''
#     # def __str__(self):
#     #     return self.name
'''для воспроизведения объекта'''
#     def __repr__(self):
#         return self.name

'''Если нет str, то будет использоваться repr'''
# a = User('John', 19)
# print(a)


# import datetime
# print(repr(datetime.date.today()))
# print(str(datetime.date.today()))


# class MyNumber(int):

#     def __init__(self, value) -> None:
#         self.value = value

#     def __add__(self, other) -> int:
#         return f'Это сложение и результат равен: {self.value + other}'
    
#     def __sub__(self, other) -> int:
#         return f'Это вычитание и результат равен: {self.value - other}'
    
#     def __mul__(self, other):
#         return f'Это умножение и результат равен: {self.value * other}'
    
#     def __pow__(self, other):
#         return f'Это возведение в степень и результат равен: {self.value ** other}'
    
#     def __truediv__(self, other) -> float:
#         return f'Это деление и результат равен: {self.value / other}'
    
    # def __floordiv__(self, other): //

    # def __mod__(self, __value: int): %

    
# object_num = MyNumber(7)
# print(object_num + 9)
# print(object_num - 9)
# print(object_num * 9)
# print(object_num ** 9)
# print(object_num / 9)
        

'''Магические методв сравнения'''
# == -> __eq__(self, other) equal - равно
# != -> __ne__(self, other) not equal - не равно
# > -> __gt__(self, other) greater than - больше чем
# < -> __lt__(self, other) less than - меньше чем
# >= -> __ge__(self, other)
# <= -> __le__(self. other)

#__invert__(self): - переворачивает итерируемый объект

# class Base:
#     def __init__(self, value):
#         self.value = value

#     def __invert__(self):
#         print('invert')
#         return self.value[::-1]
    
#     def __str__(self):
#         return self.value
    
# b = Base('hello world')
# res = ~b
# print(~b)

#__getattribute__(self, item) 
# (item - атрибут, к которому идет обращение) - автоматически вызывается при получения свойства класса с именем item

# s = 'hello'
# s.lower
# s.__getattribute__('lower')

#__getattribute__(self, item) - автоматически вызывается при получении несуществующего свойства item класса или экземпляра (когда атрибут не найден)

#__setattr__(self, key, value)- вызывается автоматически при изменении свойства класса или объекта(при присвоении значения атрибуту)

#__delattr__(self, item) - вызывается автоматически при удалении свойства item(не важно: существует оно или нет)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __getattribute__(self, item):
#         print('getattribute')
#         return super().__getattribute__(item)
    
#     def __setattr__(self, name, value):
#         print('setter')
#         super().__setattr__(name, value)

#     def __getattr__(self, item):
#         print('getattr')

#     def __delattr__(self, item):
#         print('delattr')
#         super().__delattr__(item)
    
# a = Point(1, 4)
# del a.y
# print(a.y)
# a.b
# a.y = 9

#__getitem__ - когда мы обращаемся в квадратных скобочках (по индексу, по ключу, делаем срез)
# s = 'Makers'
# # s[0]
# print(s.__getitem__(0))

# dick_ = {'a': 1, 'b': 2}
# print(dick_.__getitem__('a'))

# __setitem__ - создает ключ со хначением, или изменяем
# __delitem__ - удаляет


# class A:
#     def __getitem__(self, index):
#         print('getitem')

#     def __setitem__(self, name, value):
#         print('setitem')
#         print(name)
#         print(value)

#     def __delitem__(self, index):
#         print('delitem')
#         print(index)

# a = A()
# a.b = [1, 2, 3]
# a[1]
# a[0] = 4
# del a[2]

        
    
    
