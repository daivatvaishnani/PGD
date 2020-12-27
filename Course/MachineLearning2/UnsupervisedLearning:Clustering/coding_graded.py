import sys
import math
sys.stdin = open('in', 'r')
sys.stdout = open('out', 'w')
n = int(input())

def isPrime(num):
	if i <= 1:
		return False
	for d in range(2, int(math.sqrt(num) + 1)):
		if num % d == 0:
			return False
	return True

for i in range(1, n+1):
	if isPrime(i):
		print(i)

cells = ["#"*n for i in range(0, n)]

for i in range(0, n):
	for j in range(0, n):
		print(cells[i][j], end='')