# 9-1 Restaurant

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name} {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} work!')


restaurant1 = Restaurant('Volt', 'Chicken')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

# 9-2 describe_restaurant()

restaurant2 = Restaurant('Lol', 'Candy')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

# 9-3 create class User


class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} {self.age}')

    def greet_user(self):
        print(f'Hello {self.first_name}!')


user1 = User('Alir', 'Kelo', '20')
user1.describe_user()
user1.greet_user()
