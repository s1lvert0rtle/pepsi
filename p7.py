prime = []
def primecheck(num):#a prime number comes first and then its multiples follow
	for n in prime: #i realise this can be better through the root(n) divisibility check too
		if num%n==0:
			return
	prime.append(num)

if __name__=='__main__':
	i=2
	while(len(prime)!=10001):
		primecheck(i)
		i=i+1
	print(prime[-1])
