import math

x = int(input("entre número entero "))
if x % 2 == 0:
    print(x, "No es primo, es numero par")
    exit(0)

i = 2
for i in range(3, int(x**(.5))+1, 2):
    print(x, "NO es primo, es divisible por", i)
    break
if x % i !=0:  
    print(x, "es primo")


 
