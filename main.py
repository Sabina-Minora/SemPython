

# n = 385916

# # Введите ваше решение ниже

# l = int(n[0]) + int(n[1]) + int(n[2])
# r = int(n[3]) + int(n[4]) + int(n[5])
# if l == r:
#     print('yes')
# else:
#     print('no')



# s = input('Введите 6-значный номер билета: ')
# if len(s) != 6:
#     print(f'Число {s} не 6-ти значное')
# else:
#     res1 = 0
#     res2 = 0
#     for i in range(len(s)//2):
#         res1 += int(s[i])
#         res2 += int(s[len(s)//2 + i])
#     if res1 == res2:
#         print(f'{s} счастливый номер')
#     else:
#         print(f'{s} не счастливый номер')

t = input('Введите номер билета: ')
l = int(t[0]) + int(t[1]) + int(t[2])
r = int(t[3]) + int(t[4]) + int(t[5])
if l == r:
    print('Yes')
else:
    print('NO')