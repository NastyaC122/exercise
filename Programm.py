<<<<<<< HEAD
um = 0
for i in range(1, 11):
    sum += i
print("Сумма чисел от 1 до 10 равна:\n",sum)
=======
import random

def generate_random_list(num_elements):
    start_range = 5
    end_range = 17
    elements = [(random.randint(start_range, end_range) * 100) for _ in range(num_elements)]
    return elements

num_elements = 27
random_list = generate_random_list(num_elements)
print(random_list)
>>>>>>> amazing_new_feature
