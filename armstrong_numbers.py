def is_armstrong(number):

	n = [int(m) for m in str(number)]
	for i in range(0,len(n)):
		n[i] = n[i]**len(n)
	print(sum(n) == number)
	return (sum(n) == number)
