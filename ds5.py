# Реализуйте алгоритм перемешивания списка

import random 
N = int(input('Введите число N '))
a=[]
for i in range(N):
    a.append(random.randint(-50, 50))
print (a)
random.shuffle(a) 
print(a)

