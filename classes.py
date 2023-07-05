'''Введение в ООП'''
# ООП (объектно ориенттрованное программирование) - парадигма (набор правил) программирование. Основывается на двух понятиях - класс и объект


'''Класс - схема/чертеж/ описание того, какими свойствами и поведением будет обладать объект одного типа'''

'''Объект - это экземплятор от класса с собственным состоянием этих свойств'''

# Свойства - обычные переменные (name = 'Tima)
# Поведение - обычные функции (методы)

# class A:
#     str = 'атрибут класса'

#     def first_method(self): # создали метод
        # self - ссылка на объект
        # pass 
# fitst_obj = A() # создали от класса А
# second = A()
# f = A()

# second.first_method()

# class Person:

    # Атрибуты класса
    # arms = 2
    # legs = 2

    # def __init__(self, name, age): # функция вызывается при создании объекта, здесь определяются атрибуты объекта. Отвечает за инилтзацию
        # Атрибуты объекта(экзумрдяра класса)
    #     self.name = name # мы добавляем в объект self новый атрибут name
    #     self.age = age

    # def add_one(self):

        # функция которя принимает объект и изменяет возраст на 1
#         self.age += 1
    
#     def __str__(self):
#         return f'{self.name} - {self.age}'

# person1 = Person('Mithat, 20')
# print(person1)
# person1.add_one()


# переменная класса - (class variable)
# переменная внутри класса (поле которое относится ко всем объектам класса)
# переменная экзеипляра класса - (instance variable) - внутри метода __init__ и относятся только объекту

'''Атрибуты класса(Атрибуты на уровне класса)'''
# переменные внутри класса 
# данные атрибуты являются статическими(делфем константой, те присваиваем значения, которые не собираемся менять в будущем)
# можно обращаться через класс, не создавая объекта(legs, arms)

'''Методы класса'''
# функции внутри класса

'''объект класса'''
# объект, экземпляр, instance класса - объект созданный по шаблону класса(перенимает все атрибуты и методы у класса)

'''Атрибуты и методы объекта'''
# атрибуты и методы, кторые есть у объекта, но их может не быть у класса

# class A:
#     varl = 'переменная класса'

#     def __init__(self):
#         self.var2 = 'переменная объекта'
# # print(dir(A))

# a = A()
# print(dir(a))

'''Класс имеет доступ только к атрибутам класса'''
'''Объект имеет доступ к атрибутам класса и к своим атрибутам'''


# class Salary:
#     nalog = 15

#     def __init__(self, zp, staj):
#         self.zp = zp
#         self.staj = staj

#     def sum_nalog(self):
#         s = self.zp * self.staj * 12 * self.nalog / 100
#         print(s)
    
#     def sum_zp(self):
#         s1 = self.zp * self.staj * 12
#         print(s1)

# a = Salary(10000, 10)
# a.sum_nalog()
# a.sum_zp

# class Car:
#     wheels = 4

#     def __init__(self, auto_owner, model, year):
#         self.owner = auto_owner
#         self.model = model
#         self.year = year
#         self.mileag = 0
    # def go(self, km):
#         self.mileag += km
#         print('yyyyyyyyyyyy')
#     def __str__(self):
#         return f'Владаелец: {self.owner} - Модель: {self.model}'

# lada =Car('Aiana', 'rx330', '1980')
# print(lada)
# lada.go(100)
# print(lada.mileag)

# get_total() add_total() sub_total() 

# class SelfBank:
#     total = 0

#     def get_total(self):
#         return self.total
# a = SelfBank()
# a.total = 1000
# print(a.get_total())

# class Student:

#     def __init__(self, name, last):
#         self.name = name
#         self.last = last
#         self.know = 0
#         self.lang = {}
#         self.books = []
#     def read_book(self, book):


#         self.books.append(book)
#     def add_points(self, point):
#         self.know += point()
#     def do_nw(self):
#         self.add_points(5)
#     def new_lang(self, lang, point):
#         if 0 < point < 100:
#             self.lang.update({lang: point})
#             self.add_points(30)
#         else:
#             raise ValueError('out of range')
        
# sam = Student('Sam', 'John')
# print(sam.know, sam.books, sam.lang)
# sam.read_book('1')
# print(sam.know, sam.books, sam.lang)
# sam.new_lang('Python', 30)
# print(sam.know, sam.books, sam.lang)
# sam.do_nw

class Student:

    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last 
        self.know = 0
        self.lang = {}
        self.books = []

    def read_book(self, book):
        self.books.append(book)
        self.add_points(10)

    def add_points(self, point):
        self.know += point

    def do_hw(self):
        self.add_points(5)

    def new_lang(self, lang, point):
        if 0 < point < 100:
            self.lang.update({lang: point})
            self.add_points(30)
        else:
            raise ValueError('out of range')


sam = Student('Sam', 'John')
print(sam.know, sam.books, sam.lang)
sam.read_book('1')
print(sam.know, sam.books, sam.lang)
sam.new_lang('Python', 30)
sam.do_hw()
print(sam.know, sam.books, sam.lang)
 
