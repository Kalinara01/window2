import json


file_path = 'data.json'

class GetMixin:
    def get_data(self):
        with open(file_path) as file:
            return json.load(file)
        
    def get_id(self):
        with open('id.txt') as file:
            id = int(file.read())
            id += 1

        with open('id.txt', 'w') as file:
            file.write(str(id))
        return id
    
class CreateMixin(GetMixin):
    def create(self):
        data = super().get_data()
        # data = []
        
        try:
            new_product = {'id': super().get_id(), 'model': input('Введите модель товара:'), 'price': int(input('Введите стоимость товара:')), 'color': input('Введите цвет товара:'), 'storage': int(input('Введите память товара:'))}
        except ValueError:
            print('Ввели некорректные данные') 
            self.create()

        else:
            data.append(new_product)
            print(data)

            with open(file_path, 'w') as file:
                json.dump(data, file)
                print('Successfully created')

class ListingMixin(GetMixin):
    def listing(self):
        print('Список телефона')
        data = super().get_data()
        print(data)
        print('End')

class RetrieveMixin(GetMixin):
    def retrieve(self):
        data = super().get_data()

        try:
            id = int(input('Введите id товара:'))
        except ValueError:
            print('Ввели некорректные данные')
            self.retrieve()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))
            if not one_product:
                print('Такого продукта нет')
            else:
                print(one_product[0])

class UpdateMixin(GetMixin):
    def update(self):
        data = super().get_data()
        try:
            id = int(input('Введите id товара:'))
        except ValueError:
            print('Ввели некорректные данные')
            self.update()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))

            if not one_product:
                print('Такого товара нет')
            
            product = data.index(one_product[0])
            choice = int(input('Что вы хотите изменить? 1 - vodel, 2 - price, 3 - color, 4 - storage:'))
            
            if choice == 1:
                data[product]['model'] = input('Введите новую модель:')
            elif choice == 2:
                try:
                    data[product]['price'] = int(input('Введите новую стоимость:'))
                except ValueError:
                    print('-----------')
                
            elif choice == 3:
                data[product]['color'] = input('Введите новый цветь :')
            
            elif choice == 4:
                try:
                    data[product]['stroge'] = int(input('Введите новый объем памяти: '))
                except ValueError:
                    print('-----------')
            else:
                print('Такого поля нет')
                self.update()
            with open(file_path, 'w') as file:
                json.dump(data, file)

class DeleteMixin(GetMixin):
    def delete(self):
        data = super().get_data()
        try:
            id = int(input('Введите id товара:'))
        except ValueError:
            print('Ввели некорректные данные')
            self.delete()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))
            if not one_product:
                print('Такого товара нет')
            product = data.index(one_product[0])
            data.pop(product)
            with open(file_path, 'w') as file:
                json.dump(data, file)
            print('Удалили')
            


                       


