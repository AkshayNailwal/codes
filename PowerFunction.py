def expo(x, n, d) :
	if x==0:
		return 0
	x = x % d
	ans=1
	while (n > 0) :
		if ((n & 1) == 1) :
			ans = (ans * x) % d
		n = n >> 1
		x = (x * x) % d
	return ans
