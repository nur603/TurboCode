#task1
# a = input("TEXT:")
# a = sorted(a)
# a = ''.join(a)
# print(f"result: {a}")

# task2
import random

# i = 1
# number = random.randint(0,50)
# print(number)
# while i <= 3:
#     a = int(input("Ваше число: "))
#     if number == a:
#         print("Угадали")
#         break
#     elif number > a:
#         print ("больше")
#     elif number < a:
#         print("меньше")   
#     i +=1 
# else:         
#     print("Game over")    

#task3
# number = random.randint(11,999)
# print(number)
# num1 = number // 100
# print(num1)
# num2 = number // 10 % 10
# print(num2)
# num3 = number % 10
# print(num3)
# print(f"Число:{number} ; Сумма:{num1+num2+num3}; Произведение:{num1*num2*num3}")    

#task4
import requests
import json
# url = ('https://webhook.site/359f9eff-48f8-44e5-91d5-8755e3f7a3d6')
# param_request = {'name': 'NUR','age':'25'}
# resG = requests.get(url,params=param_request) #GET
# print(resG.text) 
# resP = requests.post(url,params=param_request) #POST
# resP = requests.post(url,headers={'name':'Nur'}) черновик
# print(resP.text) черновик

#task5
# url = ('https://webhook.site/359f9eff-48f8-44e5-91d5-8755e3f7a3d6')
# res = requests.get(url)
# print(res.text)