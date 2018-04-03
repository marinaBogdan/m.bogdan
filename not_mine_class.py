import random

dishes_string = input('What would you like? ')
dish_list = []

for dish in dishes_string.split(','):
    dish_list.append(dish.strip())

unique_dishes = set(dish_list)

def calc_time():
    return random.randint(0, 60)

class DishesList():

    @staticmethod
    def dots(dish_name):
        return dish_name.ljust(20, '.')

    @staticmethod
    def prepare_for_print(dish_name):
        return DishesList.dots(dish_name.capitalize()) + str(calc_time())
        + ' min'
        
for dish1 in unique_dishes:
    print(DishesList.prepare_for_print(dish1))
