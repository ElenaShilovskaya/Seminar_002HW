# Реализуйте алгоритм перемешивания списка.
# В виду отсутствия прямого запрета на использование методов...
import random
first_list = [1, 2, 3, 4, 5]
print ("first_list : " + str(first_list))
mixed_list = random.sample(first_list, len(first_list))
print ("mixed_list : " + str(mixed_list))