'''Основыне принципы ООП: Инкапсуляция'''

# class Phone:
#     num = '+996 771583090'

#     def print_num(self):
#         print(f'Номер телефона: {self.num}')

# my_phone = Phone()
# my_phone.print_num()
'''связь поведения объекта с его данными'''

'''Инкапсуляция - принцип ООП, у которого две трактовки
1. Объединение всех свойств и методов в одну капсулу (класс)
2. Органичение доступа к методам или атрибутам (сокрытие данных от внешнего воздействия)
'''

# Инкапсуляция как управление доступом

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# pt = Point(2,3)
# pt.x = 'coord'
# pt.y = 'hello'
# print(pt.x, pt.y)

# 3 модификатора доступа
# 1. public - публичный (данные доступны всем) - x, y
# 2. _protected - защищенный (с одним подчеркиванием) (данные доступны как внутри класса, так и дочерних классов) - _x, _y
# 3. __private - приватный (служит для оращения внутри класса) - __x, __y

# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y

# pt = Point(3, 4)
# print(pt._x, pt._y)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
    #     self.__y = y

    # def p(self):
    #     print(self.__x)

    # def set_coord(self, x, y):
    #     if type(x) in (float, int) and type (y) in (float, int):
    #         self.__x = x
    #         self.__y = y
    #     else:
    #         raise ValueError ('Координаты должны быть числами')
        
    # def get_coord(self):
    #     return self.__x, self.__y


# pt = Point(3, 4)
# pt.set_coord(6, 6)
# print(pt.get_coord())

'''геттеры и сеттеры (интерфейсные методы) - через них предполагается работа с защищенными и приватными данными.
Они используются для получения и установки значений (чтобы добавить логику проверки и избежать прямого доступа к этои атрибутам)
'''

# class P:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def dicplay_info(self):
#         print(f'{self.name}, {self.age}')

# john = P('John', 24)
# john.dicplay_info()
# john.age = 'Snow'
# john.dicplay_info()

# @property - для getattr
# @название.setter - setter

# class P:
#     def __init__(self, name, age):
#         self.name = name 
#         self._age = age

#     '''декораторы property делает из метода атрибут'''
#     @property    
#     def age(self):
#         return self._age
    
#     @age.setter
#     def age(self, new_age):
#         if type(new_age) != int:
#             raise ValueError('kkkk')
#         if new_age > 0 and new_age < 120:
#             self._age - new_age
#         else:
#             raise ValueError('llll')
        
#     @age.getter
#     def age(self):
#         return self._age
        
# p = P('hello', 12)
# # print(p.age)
# p.age = 99
# print(p.age)

# deleter - удаление атрибутов

# class Car:
#     def __init__(self, model):
#         self.__model = model
#     model = property(lambda self: self.__model)

# bmw = Car('BMW')
# print(bmw.model)


'''Анотация свойств'''
# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius

#     def get_radius(self):
#         print('Getter')
#         return self.__radius
    
#     def set_radius(self, value):
#         print('Setter')
#         if type(value) in (int, float):
#             self.__radius = value
#         else:
#             raise ValueError('Invaalid')
        
#     def del_radius(self):
#         print('Deletter')
#         del self.__radius
#     radius = property(get_radius, set_radius, del_radius, doc = 'The private radius property')

# circle = Circle(23)
# circle.radius = 99
# print(circle.radius)
        
# class PrivateProject:
#     __github_link = 'hello'
#     __developers = ['Aiana', 'Mithat']

#     def __init__(self, username):
#         self.username = username
    
#     @property
#     def get_link(self):
#         if self.username in self.__developers:
#             print(self.__github_link)
#         else:
#             print('Forbidden')

# pp = PrivateProject('hello')
# pp.get_link

# class User:
#     def _create_user(self, email, password):
#         self.email = email
#         self.__pasword = password

#     def creat_user(self, email, password):
#         self.is_superuser = False
#         self._create_user(email, password)
#     def create_superuser(self, email, password):
#         self.is_superuser = True
#         self._create_user(email, password)
    
#     def admin_login(self, password):
#         if self.is_superuser == True:
#             if password == self.__pasword:
#                 print('Successfully loggedin')
#             else:
#                 print('Invalid password')
#         else:
#             print('Forbidden')
# o1 = User()
# o2 = User()
# o1.create_superuser('Kalinara@gmail.com', '123456')
# o2.creat_user('hello', '1234')
# o1.admin_login('123456')
# o2.admin_login('1234')

# class Student:
#     def list_(self):
#         a_list = input('Введите значение').split()
#         l = list(map)


# class Duck:
#     def quak(self):
#         print('Quaaaak')
    
#     def info(self):
#         print('whire and grey color')

# class Person:
#     def quck(self):
#         print('Person imitates a duck')
    
#     def info(self):
#         print('blue eyes, brow hair')

# def a(obj):
#         obj.quck()
#         obj.info()

# donald = Duck()
# sam = Person()
# a(donald)
# a(sam)
# donald.quak()
# donald.info()
# print('========')
# sam.quck()
# sam.info()



     

        











