class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"Животное {self.name} издает звук")

    def eat(self):
        print(f"Животное {self.name} ест")

class Bird(Animal):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color
        self.type = "птица"

    def make_sound(self):
        print(f"Птица {self.name} кричит")

    def eat(self):
        print(f"Птица {self.name} питается зернами")

    def add_zoo(self, list_animals):
        list_animals.append(self)




class Mammal(Animal):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color
        self.type = "зверь"

    def make_sound(self):
        print(f"Зверь {self.name} рычит")

    def eat(self):
        print(f"Зверь {self.name} питается мясом")

    def add_zoo(self, list_animals):
        list_animals.append(self)

class Reptile(Animal):
    def __init__(self,name,age,is_venomous):
        super().__init__(name,age)
        self.is_venomous = is_venomous
        self.type = "рептилия"

    def make_sound(self):
        print(f"Рептилия {self.name} шипит")

    def eat(self):
        print(f"Рептилия {self.name} питается растениями")

    def add_zoo(self, list_animals):
        list_animals.append(self)



class ZooKeeper():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def feed_animal(self, animal):
        try:
            print(f"Сотрудник {self.name} кормит {animal.type} {animal.name}")
        except:
            print(f"Сотрудник {self.name} кормит {animal.name}")

    def add_zoo(self, list_employees):
        list_employees.append(self)


class Veterinarian():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def heal_animal(self, animal):
        try:
            print(f"Сотрудник {self.name} лечит {animal.type} {animal.name}")
        except:
            print(f"Сотрудник {self.name} лечит {animal.name}")

    def add_zoo(self, list_employees):
        list_employees.append(self)


class Zoo():
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} добавлен в зоопарк")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Работник {employee.name} добавлен в зоопарк")

    def show_animals(self):
        print(f"Животные в {self.name}: ")
        for animal in self.animals:
            print(f"- {animal.type} {animal.name}")

    def show_employees(self):
        print(f"Работники в {self.name}: ")
        for empployee in self.employees:
            print(f"- {empployee.name}")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

bird1 = Bird("Кеша",3, "зеленый")
lion1 = Mammal("Эдвин", 4, "белый")
snake1 = Reptile("Кобра", 3, True)

animals=[bird1, lion1, snake1]
animal_sound(animals)


sotr1 = ZooKeeper("Иван", 60, 50000)
sotr2 = ZooKeeper("Мария", 32, 80000)

vet1 = Veterinarian("Анна", 25, 100000)

sotr1.feed_animal(bird1)
sotr2.feed_animal(bird1)

vet1.heal_animal(bird1)


my_Zoo = Zoo("Мой зоопарк")
my_Zoo.add_animal(bird1)
my_Zoo.add_animal(lion1)
my_Zoo.add_animal(snake1)

my_Zoo.add_employee(sotr1)
my_Zoo.add_employee(sotr2)

my_Zoo.show_animals()
my_Zoo.show_employees()



