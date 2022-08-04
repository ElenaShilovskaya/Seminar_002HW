# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму

def get_res(n):
    return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]

n = int(input('Введите число: ')) 
nums = get_res(n)
print(nums)
print(round(sum(nums), 5))
