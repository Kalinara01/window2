'''Принцип ООП: Астракция'''
'''Принцип ООП, в котором создаются классы пустышки,
где задаются названия атрибутов и методов, чтобы не забыть переопределить их в дочерних классах
'''

from abc import ABC, abstractmethod

# class A(ABC):
#     def method1(self):
#         print('обычный метод')
#     @abstractmethod
#     def method2(self):
#         pass
#         # print('Я обстрактный метод')# обычно не опеределяют логику

# class B(A):
#     def method2(self):
#         print('переопределили')

# b = B()

# from abc import ABC, abstractmethod, abstractproperty

# class AbctractAnimal(ABC):

#     @abstractproperty
#     def legs(self):
#         pass

# class Dog(AbctractAnimal):
#     legs = 4

#     def voice(self):
#         print(' ГАВ-гав')

# # obj = Dog()
# # obj = Dog()
# # print(obj.legs)

# # @abstractmethod - метод, у которого есть объявление, но нет реализации (объявили, но нет логики)

# # @abstractproperty - метод, но будет переопределен как атрибут

# class People(ABC):
#    @abstractmethod
#    def move(self):
#        pass
   
#    @abstractmethod
#    def breathe(self):
#        pass
   
#    @abstractmethod
#    def eat(self):
#        pass
   

#    @abstractmethod
#    def sleep(self):
#        pass
   
#    @abstractproperty
#    def name(self):
#        pass
   
# class Person(People):
#     name = None

#     def move(self):
#         print('Иду')

#     def breathe(self):
#         print('Иду')

#     def eat(self):
#         print('Иду')

#     def sleep(self):
#         print('Иду')

# a = People()
# a.move()


# class Abst(ABC):

#     @abstractmethod
#     def get_info():
#         pass

#     @abstractmethod
#     def set_info():
#         pass
# class IdenticateMixin:

#     def identiicate(self, year):
#         if int(year) < 2010:
#             print('This is old car')
#         else:
#             print('This is bew car')

# class BaseAuto(Abst):
#     def __init__(self, model, year, owner):
#         self.m = model
#         self.y = year
#         self.o = owner

#     def get_info(self):
#         return f'Model: {self.model}\n Year: {self.year}'
    
#     def set_info(self, owner):
#         self.__owner = owner

#     def get_owner(self):
#         return self.__owner
    
# a = BaseAuto('mers', '2022', 'Sam')
# print(a.get_info())
# a.set_info('John')
# print(a.get_owner())


# class Automobile(BaseAuto):
#     def __init__(self, model, year, owner, color, brand) -> None:
#         super().__init__(model, year, owner)
#         self.color = color
#         self.brand = brand

#     @property
#     def owner(self):
#         return self.__BaseAuto__owner
    
#     @owner.setter
#     def owner(self, new_owner):
#         self._BaseAuto__owner = new_owner

#     @owner.deleter
#     def owner(self):
#         self._BaseAuto__owner = 'Nobody'

# a = Automobile('mers', '2022', 'Sam', '', 'black')
# print(a.owner)
# a.owner = 'John'
# del a.owner
# print(a.owner)
# a.identicate(a.year)

# class BaseStudent(ABC):
#     @abstractmethod
#     def info_(self):
#         ...

# class FacMixin:
#     def cool(self, faculty):
#         if faculty == 'IT':
#             print('cool')
#         else:
#             print('not bad')

# class Student(BaseStudent, FacMixin):
#     def __init__(self, name, last_name, factulty, class_):
#         self.name = name
#         self.last_name = last_name
#         self.factulty = factulty
#         self.__class_ = class_

#     def info_(self):
#         print(f'name: {self.name}')
    
#     @property
#     def class_(self):
#         return self.__class_
    
#     @class_.setter
#     def class_(self, new_class):
#         self.__class_ = new_class

# a = Student('Sam', 'D', 'IT', 4)
# a.info_()
# a.cool(a.factulty)
# a.class_ = 3
# print(a.class_)



class Person: 
    def __init__(self): 
        self.__name = None 
        self.__last_name = None 
        self.__age = None 
        self.__email = None 
    @property 
    def name(self): 
        return self.__name 
    @name.setter 
    def name(self, value): 
        self.__name = value 
    @property 
    def last_name(self): 
        return self.__last_name 
    @last_name.setter 
    def last_name(self, value): 
        self.__last_name = value 
    @property 
    def age(self): 
        return self.__age 
    @age.setter 
    def age(self, value): 
        self.__age = value 
    @property 
    def email(self): 
        return self.__email 
    @email.setter 
    def email(self, value): 
        self.__email = value 
john = Person() 
print(john.name) 
print(john.last_name) 
print(john.age) # None 
print(john.email) # None 
john.name = 'John' 
john.last_name = 'Snow' 
john.age = 30 
john.email = 'johnsnow@gmail.com' 
print(john.name)