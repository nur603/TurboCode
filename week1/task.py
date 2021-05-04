# -*- coding: utf-8 -*-
#easy1
# n = int(input("Количество школьников = "))
# k = int(input("Количество яблок = "))
# c = k / n
# d = k % n
# print(int(c),d)

#easy2
# class1 = int(input("количество школьников в классе1 = "))
# class2 = int(input("количество школьников в классе2 = "))
# class3 = int(input("количество школьников в классе3 = "))
# sum = (class1 + class2 + class3)/2
# if sum % 2:
#     sum+=1
# sum = round(sum)
# print(sum)

#easy3
# a1 = int(input("Введите цифру = "))
# a2 = int(input("Введите цифру = "))
# a3 = int(input("Введите цифру = "))
# if a1 == a2 == a3:
# 	print(3)
# elif    a1 == a2 or a1 == a3 or a2 == a3:
# 	print(2)
# else:
# 	print(0)

# easy4
# a = []
# n = int(input("Укажите кол-во = "))
# counter = 0
# for i in range(n):  
#     new_elem = int(input())
#     a.append(new_elem)
#     if new_elem == 0:
#       counter += 1
# print(f"Количество нулей =  {counter}")

#medium5
# file = open("hello.txt", "w")
# for i in range (0,100):
# 	file.write('Я программист\n')
# print("Готово")
# file.close()

#medium6
# f = open('teamname.txt', 'r') 
# f = f.read()
# f = f.splite()
# print(f)

# f = open('teamname.txt', 'r', encoding = 'utf-8')
# f = f.read()
# f = f.split()
# counter1 = 0
# counter2 = 0
# for i in range(0, len(f)):
# 	if f[i] == 'ElonMars':
# 		counter1 = int(counter1) + 1
# 		counter2 = int(counter2) + 1
# 	elif f[i].upper() == 'ELONMARS':
# 		counter2 = int(counter2) + 1
# print(f"ElonMars = {counter1} Общее {counter2}")