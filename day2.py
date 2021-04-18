# def my_func():
# 	a = 123
# 	print(a)
# 	print("success")
# 	return a
# print(my_func())	


# def my_func(name, surname):
#   print(f"Hello {name} {surname}")

# # b = my_func()
# # print(my_func())
# my_func('Berik', 'Serikovich')

# def task1(a,b):
# 	return a * b     

# print(task1(3,6))	

# def func(a, b=3,c=4):
# 	print(a, b, c)
# a = 123
# func(a, c=9)


# import my_module as mmod

# age = input ("Your age?\n")

# mmod.night_club(age)

# import arif as mt
# import str_work as st

# print(mt.plus(1,3))
# print(mt.minus(4,3))
# print(st.add_str('Egor','Berikov'))
#datetime
# x = datetime.datetime(2020, 5, 17)
# print(x)
# print(x.strftime("%d.%m.%Y %H:%M"))

# from openpyxl import load_workbook

# wb = load_workbook('table.xlsx')
# # print(wb.sheetnames)
# sheet = wb.get_sheet_by_name('users')
# print(sheet)
# # print(sheet['A2'].value)
# sheet['A2'].value = 'Beka'
# # print(sheet['A2'].row)
# # print(sheet['A2'].column)
# # print(sheet['A2'].coordinate)

# for i in range(1, 5):
#      print(i, sheet.cell(row=i, column=1).value)

# wb.save('table.xlsx')

# wb = load_workbook('table2.xlsm')
# print(wb.sheetnames)
# sheet = wb.get_sheet_by_name('Database')
# # print(sheet['K4'].value)
# sum1 = 0
# for i in range(4, 25):
# 	a = sheet.cell(row=i, column=11).value
# 	# a = heet.cell(row=i, column=4).value
# 	sum1 = sum1 + a
# print(sum1)
# 	# a = int(a)

import requests
import json

# res = requests.get('https://jsonplaceholder.typicode.com/posts')
# # print(res.text)
# response = res.text
# response = json.loads(response)
# # print(type(response))
# # for i in response:
# # 	if i['userId'] == 1:
# # 		print(i['title'])

# # for i in range(0,len(response)):
# # 	if response[i]['userId'] == 1:
# # 		print(response[i]['title'])

# for i in response:
# 	if i['title'] == 'non est facere':
# 		print(i['body'])


res = requests.get('https://jsonplaceholder.typicode.com/users')
# print(res.text)
response = res.text

response = json.loads(response)
for i in response:
	if i['id'] == 4:
		print(i['address']['geo'])















