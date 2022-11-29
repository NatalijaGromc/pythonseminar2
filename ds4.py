# 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random
N = int(input('Введите число N '))
a=[]
for i in range(N):
    a.append(random.randint(-N, N))
print (a)
prod = 1
with open('file.txt','r') as data:
    for line in data:
            prod = prod*a[int(line)]
print(prod)