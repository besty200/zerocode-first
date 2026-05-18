print("ЗАДАНИЕ 1")
my_tasks = []
class Task():
    def __init__(self, description, deadline, status=False):
        self.description = description
        self.deadline = deadline
        self.status = status

    def add_task(self):
        self.status = False
        my_tasks.append(self)

    def change_status(self):
        if self.status == False:
            self.status = True
            print(f"Задача {self.description} выполнена успешно")
        else:
            self.status = False


def print_tasks():
    print("Текущие задания:")
    for i in my_tasks:
        if i.status==False:
            print(f"{i.description} выполнить до {i.deadline}")

task1 = Task("Помыть машину", "29.11.2025")
task1.add_task()

task2 = Task("Купить продукты", "30.11.2025")
task2.add_task()

print_tasks()
print(f"Выполняем задачу {task1.description}")
task1.change_status()

print_tasks()

print()
print("ЗАДАНИЕ 2 - дополнительное")
class Store():

    def __init__(self, name, address, items=None):
        self.name = name
        self.address = address
        if items is None:
            self.items = {}
        else:
            self.items = items


    def add_product(self, product, price):
        self.items[product]=price

    def delete_product(self, product):
        if product in self.items:
            del self.items[product]
        else:
            print(f"Удалить товар невозможно. Товар \"{product}\" отсутствует в ассортименте магазина {self.name}")

    def get_price(self, product):
        if product in self.items:
            print(self.items[product])
        else:
            print("None")

    def update_product_price(self, product, price):
        self.items[product] = price


store1 = Store("Магнит","ул. Ленина 101")
store1.add_product("бананы",50)
store1.add_product("курица",150)
store1.add_product("яблоки",40)

store2 = Store("Пятерочка","ул. Комсомольская 12")
store2.add_product("арбуз",45)
store2.add_product("морковь",65)
store2.add_product("укроп",140)

store3 = Store("Перекресток","ул. Ерошевского 74")
store3.add_product("йогурт",55)
store3.add_product("сок",180)
store3.add_product("яйца",110)

store1.delete_product("конфеты")

print(store1.items)
store1.get_price("бананы")
store1.get_price("банаdgvfhdны")

store1.update_product_price("бананы", 70)
print(store1.items)
store1.get_price("бананы")
store1.get_price("апельсины")






