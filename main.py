 # -*- coding: utf-8 -*-
# Hello World
# print("Hello Elon Mars")
# '''
# print("Error") 
# '''
# print("Salem")

#data types

# string
# a = 'asdasd'
# b = "asdasdasd"
# c = '''asdasdasd'''

# #int
# a = 1123

# # float
# a = 23.123

# a1 = [1,2,3, '223']

# d = {
#   'asd': 123,
#   '23': 233
# }

# # boolean
# a = True
# a = False

# print(type()) узнать тип

# a = '123'  преобразовывать 
# a = str(a)
# print(a)
# print(type(a))
# x = range (6)
#print("x")

# a = 2+2
# b = 6-2
# c = 2*2
# d = 10/2
# j = 10%3
# print(a,b,c,d,j)

# task1
# a = 1
# b = '1'
# b = float(b)
# c = 1.14
# d = a + b + c
# print(round(d, 2))

#print error
#git init
# git remote set-url 'https'
# git add .
# git status
# git commit -m 'message'
# git remote add origin https
# git push origin master

#input task 

# a = input ("Number \n")
# b = input ("Number \n")
# c = input ("Number \n")

# d = int(a) * int(b) * int(c) 
# # str d = a + b + c 
# print(d)

# r = input ("r = ")
# r = int(r)
# p = 3.14
# S = p * r**2
# print (S)

# name = input ("name = ")
# a = f"Hello {name}"
# print(a)
# txt  = ("Hello Banana greps apple Banana banana")
# upperall = txt.upper()
# print(upperall)
# replace = upperall.replace("BANANA", "apple")
# print(replace)
# password1 = '2222'#Jack
# password2 = '3333'#Nick

# user_input = input("Введи пароль")

# if user_input == password1:
#   print('Hello Jack')
# elif user_input == password2:
#   print('hello Nick')
# else:
#   print('wrong password!')

# Number1 = input ("Vvedite num1 = ")
# Oper = input ("Vyberite oper  +, -, *, /, = ")
# Number2 = input ("Vvedite num2 = ")
# Number1 = int(Number1)
# Number2 = int(Number2)
# Sex = input("Input your sex (female, male):")
# Age = input("Input your age:\n")
# Age = int(Age)
# if Sex == "female" and Age >= 18:
#   print("Come in")
# elif Sex == "male" and Age >= 21:
#   print("Come in")
# elif (Sex == "male" and Age <0) or (Sex == "female" and Age<0):
#   print ("Error")
# else:
#   print("Go home!")
# # if Oper == "+":
# 	print(Number1 + Number2)
# elif Oper == "-":
# 	print(Number1 - Number2)
# elif Oper == "*":
# 	print(Number1 * Number2)
# elif Oper == "/":
# 	print(Number1 / Number2)
# else:
# 	print("Error")			
# gen = input("Choose your gender\n")
# age = input("What is your age\n")
# if int(age) <= 0:
#   print("Write the correct age")
#   age = input("What is your age\n")

# gen = str(gen).upper()
# if (gen == "W" and int(age) >= 18) or (gen == "M" and int(age) >= 21):
#   print("Ote ber")
# else:
#   print("Kait uine")
# Gender = input ("Girl and Boy? \n")
# Age = input ("Your age?\n")
# GenUp = Gender.upper()
# Age = float(Age)
# if GenUp == "GIRL" and Age >=18:
# 	print("Open")
# elif GenUp == "GIRL" and Age <=18:
# 	print("Go home")
# elif GenUp == "BOY" and Age >=21:
# 	print("Open")
# elif GenUp == "BOY" and Age <=21:
# 	print("Go home")
# else:
# 	print("ERROR")	
#dict
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])
# # ['apple', 'banana', 'cherry', 'orange']

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[4:])
# # ["kiwi", "melon", "mango"]

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thislist[2] = 'KKKKK'
# fruit = thislist[3]
# print(thislist)
# print(fruit)

#d = {
#   'name' : 'Egor',
#   'surname': 'EgorUlyKotiBar',
#   'pas': 123123,
#   'WW': True,
#   'array': [12,2,3,24,3],
#   'dd': {
#     '2level': 'Egor2',
#     '2pas': 21312
#   }
# }

# a = input("Vvedite = ")
# b = input("Vvdeite = ")
# print(a)
# print(b)
# a = int(a)
# b = int(b)
# a = a + b
# b = a - b
# a = a - b
# a, b = b , a
# print(a)
# print(b)

# num = [1,2,7,4,5,6,3]
# txt = ["mango", "banan", "mandarin", "alma"]
# num.pop(2)
# num.sort()
# txt.sort()
# num = sorted(num)
# txt = sorted(txt)
# print(num)
# print(txt)

# i = 0
# while i < len(thislist):
#   # print(thislist[i])
#   if thislist[i] == 'cherry':
#     print(thislist[i])
#   else:
#     print('other fruit')
#   i += 1#i = i + 1

# i = 0
# while i < 2:
#   j = 0
#   while j < 2:
#     print('this is I', i)
#     print('this is J', j)
#     j += 1
#   i += 1
# print(j)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# for i in thislist:
# 	print(i) 
# 	if i == 'orange':
# 		break

# txt = '''asd awd awd awD awd banana BanAna bananA apple asd asdw ad da BananA asd awd awd awD awd banana BanAna bananA apple asd asdw ad da BananA asd awd awd awD awd banana BanAna bananA apple asd asdw ad da BananA'''
# txtup = txt.upper()
# # print(txt)
# # print(txtup)
# txt = txt.split(' ')
# txtup = txtup.split(' ')
# for x in range(0, len(txtup)):
# 	if txtup[x] == "BANANA":
# 		txt[x] = "BANANA"
# txt = ' '.join(txt)
# print(txt)


# txt = txt.split(' ')
# txt = txt.upper()
# for x in txt == "BANANA"
	

# sp = sp.split(' ')

# sp = ' '.join()
# print(txt)
# i = 0
# a = a.split()
# while i < len(a):
#   if a[i].lower() == 'banana':
#     a[i] = 'BANANA'
#   i += 1# txt = txt.split(' ') #txt = ['asd', 'awd', 'awd', 'awD', 'awd', 'banana', 'BanAna', 'bananA', 'apple', 'asd', 'asdw', 'ad', 'da', 'BananA', 'asd', 'awd', 'awd', 'awD', 'awd', 'banana', 'BanAna', 'bananA', 'apple', 'asd', 'asdw', 'ad', 'da', 'BananA', 'asd', 'awd', 'awd', 'awD', 'awd', 'banana', 'BanAna', 'bananA', 'apple', 'asd', 'asdw', 'ad', 'da', 'BananA']

# a = ' '.join(a)
# print(a)

# for i in range(1,11):
# 	if i % 2 == 0:
# 		print(i)
# x1 = [1,2,3,4,5]

# x2 = [1,5,10]
# for i in range(0,len(x1)):
#  for j in range(0,len(x2)):
#   if x1[i] == x2[j]:
#    a = x1[i]
#    b = x2[j]
#    print(a,b)

# a1 = [1,2,3,4,5]
# a2 = [1,2,10,5]
# for a in range(0,len(a1)):
# 	for b in range(0,len(a2)):
# 		if a1[a] == a2[b]:	
# 			print(a1[a])	


# try:
# 	a = input("Num = ")
# 	print(int(a) * 10)
# except Exception as e:
# 	print(e, "ERROR! Enter a number")












