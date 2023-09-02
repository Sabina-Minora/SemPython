# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

# list_1 = [1, 2, 3, 4, 5] 
# k = 6 

list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
k = 10

# for i in range(len(list_1)): 
#     if list_1[i] < k: 
#         num = -k 
#     else: num = num + 0 

# if list_1[i] >= k and list_1[i] - k <= num - k: 
#     num = list_1[i] 

# elif list_1[i] <= k and num - k <= list_1[i] - k: 
#     num = list_1[i] 

# print(num)


def find_near(list_1, k):
    list_1.sort()
    near_num = list_1[0]
    for num in list_1:
        if abs(num - k) < abs(near_num - k):
            near_num = num
        if num > k:
            break
    return near_num

print(find_near(list_1, k))

