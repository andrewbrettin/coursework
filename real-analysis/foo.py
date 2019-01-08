def foo(x):
	an = x
	for i in range(1,10):
		print an
		an = (0.5)*(an + 2/an)
print("\nFoo 0.5")
foo(0.5)
print("\nFoo 1")
foo(1)
print("\nFoo 1.25")
foo(1.25)
print("\nFoo 5")
foo(5)