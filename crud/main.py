# Greate Read Update Delete (CRUD)

# class GreateMixin:
#     def create(self,todo, key):
#         if key in self.todos:
#             return 'Задача под таким ключем уже существует'
#         else:
#             self.todos[key] = todo
#             return self.todos

# class DeleteMixin:
#     def delete(self, key):
#         print(self.todos.pop(key))

# class ReadMixin:
#     def read(self):
#         print(sorted(self.todos.items()))

# class UpdateMixin:
#     def update(self,key, new_value):
#         self.todos[key] = new_value


# class Notes (GreateMixin, DeleteMixin,ReadMixin, UpdateMixin):
#     todos = {}

# task = Notes()
# task.create('read a book', 2)
# task.create('homework', 1)
# task.update(1, 'jfire')
# task.delete(2)
# task.read()

from views import CreateMixin
from views import ListingMixin
from views import RetrieveMixin
from views import UpdateMixin
from views import DeleteMixin

class Product(CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin, DeleteMixin):
    pass

product = Product()
# product.create()
# product.listing()
# product.retrieve()
# product.update()
product.delete()
