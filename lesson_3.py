name = input('Input name: ')
age = int(input('Input age: '))
phone_number = input('Input phone_number: ')


if age > 0:
	if 0 < age <= 2:
		print("1")
		vaccine_answer = input ()
		if vaccine_answer == 'yes':
			print('ok')
		elif vaccine_answer == 'no':
			print('get vaccine')
		else:
			print ('error')

	elif 2 < age <= 6:
		print('2')
	elif 6 < age <= 12:
		print ('3')
	elif 12 < age <= 18:
		print ('4')
	else:
		print('5')
else:
	print ('Your age shoud be positive')