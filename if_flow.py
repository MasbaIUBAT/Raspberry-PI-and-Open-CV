while True:
	try:
		x = int(input("Please enter #:"))
		if x<0:
			print ('Negative')
		elif x == 0:
			print('Zero')
		elif x == 1:
			print('Single')
		else:
			print('More')
	except ValueError:
		print ("Please enter integer only.")
		pass
	except KeyboardInterrupt:
		print("bye bye")
		exit()

