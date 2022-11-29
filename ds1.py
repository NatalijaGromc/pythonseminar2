# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11
a = input('введите а ')
# print(a.isdigit())
sum=0
for i in range(len(a)):
    if a[i].isdigit():
        sum=sum+int(a[i])

print(sum)
    
