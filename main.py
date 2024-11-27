import bubble_sorter
import random
random_numbers = []
for i in range(100):
    random_numbers.append(random.randrange(0,100))
print("-->", random_numbers)
bubble_sorter.sort(random_numbers)
print("Sorted -> ",random_numbers)