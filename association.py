'''Принцип ООП: Ассоциация'''
# принцип ООП, в котором два класса связанны с друг другом

# агрегация - слабая свзяь
# композиция сильная свзяь

# A - КОМПОНЕНТ
# l
# l
# l
# V
# В - СОСТАВНОЙ:

# class Engine:
#     pass

# class Wheel:
#     pass

# class Freshener:
#     pass

# class Car:

#     def __init__(self, freshener) -> None:
#         self.freshener = freshener
#         self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()] # - композиция
#         self.engine = Engine()

# elochka = Freshener() # - агрегация

# car = Car(elochka)
# del car
# print(elochka)
# print(car.__dict__)
        
# Пример композиции
# class Salary:
#     def __init__(self, pay) -> None:
#         self.pay = pay
#     def getTotal(self):
#         return self.pay * 12
    
# class Employee:
#     def __init__(self, pay, bonus) -> None:
#         self.pay = pay
#         self.bonus = bonus
#         self.salary = Salary(self.pay)

#     def getTotalSalary(self):
#         return 'Total ' + str(self.salary.getTotal() + self.bonus)
    
# # employee = Employee(100, 90)
# # print(employee.getTotalSalary())

# class Salary:
#     def __init__(self, pay) -> None:
#         self.pay = pay
#     def getTotal(self):
#         return self.pay * 12
    
# class Employee:
#     def __init__(self, pay, bonus) -> None:
#         self.pay = pay
#         self.bonus = bonus
#         self.salary = Salary(self.pay)

#     def getTotalSalary(self):
#         return 'Total ' + str(self.salary.getTotal() + self.bonus)
    
# salary = Salary(100)
# employee = Employee(salary, 90)
# print(employee.getTotalSalary())
    

# class Battery:
#     _power = 100

#     def charge(self):
#         if self._power < 100:
#             self._power = 100

# class Iphone:
#     def __init__(self, color, battery) -> None:
#         self.color = color
#         self.b = Battery()
#         #когда мы создаем объект от другого класса внутри класса - композиция

# class Nokia:
#     def __init__(self, color, battery) -> None:
#         self.color = color
#         self.b = battery
    
# ip = Iphone('red')
# # print(ip.battery)
# # del ip
# # # при удалении iphone вместе с ним удаляется батарейка

# battery = Battery()
# nokia = Nokia('black', battery)
# # print(nokia.battery)

# del nokia
# print(battery)
        
# class ExportJSON:
#     def export(self, obj):
#         return f'Класс ExportJSON.\n"имя": {obj.name}\n"порода": {obj.breed}'
    
# class ExportCSV:
#     def export(self, obj):
#         return f'Класс ExportCSV.\nимя: {obj.name}\n"порода": {obj.breed}'
    
# class Pet:
#     def __init__(self, name) -> None:
#         self.name = name

# class Dog(Pet):
#     def __init__(self, name, breed=None) -> None:
#         super().__init__(name)
#         self.breed = breed

# class ExportDogData(Dog):
#     def __init__(self, name, breed=None, exporter=None) -> None:
#         super().__init__(name, breed)
#         self.exporter = exporter

#     def export(self):
#         return self.exporter.export(self)
    
# dog = ExportDogData('Граф', 'дворняга', exporter = ExportJSON)
# print(dog.export())

# class GameCharacter:
#     def __init__(self, name, health, level):
#         self.name = name
#         self.health = health
#         self.level = level
#     def speak(self):
#         print(f'Hi, my name is {self.name}')
    
# class Vilain(GameCharacter):
#     def speak(self):
#         super().speak()
#         print('and i will kill you')

#     def kill(self, obj):
#         obj.health = 0
#         print("Bang-bang, now you're dead")

# sam = GameCharacter(100, 10, 'Sam')
# john = Vilain(100, 15, 'John')
# sam.speak()
# john.speak()
# john.kill(sam)
# print(sam.health)

        
        
    

