def max_product(a):
	mx = max(a)
	a.remove(mx)
	next_mx = max(a)
	return mx * next_mx

print(max_product([56, 335, 195, 443, 6, 494, 252]))