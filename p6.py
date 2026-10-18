def find_diff(n):
	sq_sum = (2*n**3+3*n**2+n)/6
	sum_sq = (n**4+n**2+2*n**3)/4
	return sum_sq-sq_sum

if __name__=='__main__':
	print(find_diff(100))
