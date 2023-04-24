# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def exponentiation(a, b):
    if a == 0 and b == 0:
        return 0
    elif b == 0:
        return 1
    elif b == 1:
        return a
    elif b > 1:
        return a * exponentiation(a, b - 1)
    
a = int(input('Введите число А > '))
b = int(input('Введите число В > '))
print(f'Число {a} возведенная в степень {b} рано {exponentiation(a, b)}')