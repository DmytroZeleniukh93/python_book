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
