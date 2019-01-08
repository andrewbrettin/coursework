def foo(a,b):
	xn2=a
	xn1=b
	for i in range(0,100):
		xn = (0.5)*(xn2+xn1)
		print str(i) + ":\t" + str(xn)
		xn2=xn1
		xn1=xn
	return xn
	
foo(0, 1)