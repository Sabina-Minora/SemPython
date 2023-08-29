
#Перевевсти десятичное число в двоичное

num = int(input('Введите число: '))
res = str()

while num > 0:
    res = str(num%2) + res
    num = num//2
print(res)