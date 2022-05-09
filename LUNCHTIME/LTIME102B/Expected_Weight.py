from fractions import Fraction
def calculate(p, q):
	mod = 998244353
	expo = 0
	expo = mod - 2
	while (expo):
		if (expo & 1):
			p = (p * q) % mod
		q = (q * q) % mod
		expo >>= 1
	return p
if __name__ == '__main__':
    for _ in range(int(input())):
        q=int(input())
        p=((q*(q+1)//2)**2)
        ans=Fraction(p,q)
        print(calculate(ans.numerator, ans.denominator))
