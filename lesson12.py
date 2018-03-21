import random

Dishes_string = input('What would you like? ')  # This is a string

# put your program here
a = set(Dishes_string.replace(' ','').split(',')) # Little debugging added
for i in a:
    random_integer = random.randint(0, 100)
    print((i.capitalize()).ljust(20,'.') + str(random_integer)+'min')
   
# your program’s end
