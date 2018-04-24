import random

dishes_string = input('What would you like? ')
dish_list = []

for dish in dishes_string.split(','):
    dish_list.append(dish.strip())

unique_dishes = set(dish_list)

def calc_time():
    return random.randint(0, 60)

class DishesList():

    def dots(dish_name):
        return dish_name.ljust(15, '.')
    
    def prepare_for_print(dish_name):
        prepared = dots(dish_name) + str(calc_time()) + 'minutes'
        return prepared

for dish1 in unique_dishes:
    print(DishesList.dots(dish_name).prepare_for_print(dish1))
