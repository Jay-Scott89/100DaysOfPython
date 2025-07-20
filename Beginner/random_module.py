import random # Documentation- https://docs.python.org/3/library/random.html
import my_module # my own values

random_int = random.randint(1, 10) # Range of integers
random_float = random.random() # Range from 0.0 - < 1.0, if you want above zero values then multiply by 10
random_real_number = random.uniform(1, 100) 

print(random_int)
print(random_float)
print(random_real_number)
print(my_module.pi)