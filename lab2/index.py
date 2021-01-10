import random
import math

def fibo(n):
	if (n == 1) or (n == 2):
		return 1
	return fibo(n - 1) + fibo(n - 2)

print('Δώστε έναν αριθμός του Fibonachi')
userNumber = int(input())
fiboNumber = fibo(abs(userNumber))
if (userNumber < 0) and (userNumber % 2 == 0):
	fiboNumber = fiboNumber * (-1)

result = False
finalResult = True

for x in range(20):
	randNum = random.randint(1, 100)
	result = (randNum ** fiboNumber) % fiboNumber == (randNum % fiboNumber)
	if result == False:
		finalResult = False

if finalResult:
	print(str(fiboNumber) + ' είναι πρώτος')
else:
	print(str(fiboNumber) + ' δεν είναι πρώτος')