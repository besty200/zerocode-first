class User():

    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__level = "user"


    # Геттеры
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    # Сеттеры
    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_name(self, name):
        self.__name = name

class Admin(User):

    def __init__(self, user_id, name, admin_access=True):
        super().__init__(user_id, name)
        self.admin_access = admin_access

    # Доп. геттер для уровня доступа администратора
    def get_admin(self):
        return self.admin_access

    def add_user(self, user, user_list):
        user_list.append(user)


    def remove_user(self, user_id, user_list):
        for user in user_list:
            if user.get_user_id()==user_id:
                user_list.remove(user)
                print(f"Пользователь {user.get_name()} с ID = {user_id} успешно удален из списка")
                return
        print(f"Пользователь с ID {user_id} не найден.")



users=[]
users_names=[]
admin1=Admin(100, "Антон",  True)
user1=User(1, "Иван")
user2=User(2, "Мария")
print(admin1.get_level())
print(admin1.get_admin())

admin1.add_user(user1, users)
print(users)
admin1.add_user(user2, users)
print(users)

admin1.remove_user(2,users)
admin1.remove_user(3,users)
for i in users:
    users_names.append(i.get_name())
print(users_names)