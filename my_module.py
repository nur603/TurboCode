def night_club(age):

	try:
		age = int(age)
		if age>=18:
			print("Open")
		else:
			print("Go home")
	except Exception as e:
		print(e,"Enter a number")