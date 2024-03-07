from functools import lru_cache

@lru_cache(maxsize=1000)
def F(n):
    if n == 1 or n == 2:
        return 1
    else:
        return F(n-1) + F(n-2)

n = int(input("Введите номер вычисляемого числа:"))
if n <= 0:
    print("Невозможно вычислить число, номер которого меньше или равен 0")
else:
    print("Число Фибоначчи под номером", n, "равно", F(n))