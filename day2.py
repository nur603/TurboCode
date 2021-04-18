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



age = input ("Your age?\n")


def night_club(age):

	try:
		age = int(age)
		if age>=18:
			print("Open")
		else:
			print("Go home")
	except Exception as e:
		print(e,"Enter a number")
			
	

night_club(age)














