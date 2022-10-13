import sympy 
import random
x=0
x=sympy(("x"))
print (sympy(x))
print ("Введите степень")
t = int(input())
b=[]
a=""
for i in range(t):
    c = int(random.uniform(0, 100))
    expr=x**i
    ##c = int(random.uniform(0, 100))*pow(x,t-i)
    a=str(c)+str(expr)+a
    b.append(a)
print(b)