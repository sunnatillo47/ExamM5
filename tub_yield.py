from math import sqrt

def tub_son(n):

	for i in range(3, int(sqrt(n))+1, 2):
		if n % i == 0:
			return False
	return True

def tubs(num):
	yield 2 #--> yagona juft tub son
	for n in range(1, num+1, 2):
		if tub_son(n) and n != 1:
			yield n

n = int(input('Son kiriting: '))
print(f"{n} sonigacha bo'lgan tub sonlar:\n{list(tubs(n))}")

