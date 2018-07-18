def fib(n):
	print ("Print a Fibonacci series up to {}".format(n))
	a, b = 0, 1
	while b<n:
		print (b)
		a, b = b , a+b

def fibo(n):
	a, b = 0, 1
	res = []
	while b<n:
		res.append(b)
		a, b = b , a+b
	return res
