import sympy 
import random
x=sympy.symbols("x")
print(x)
print ("Введите степень")
t = int(input())
a=""
for i in range(t):
    c = random.randint(0, 100)
    expr=x**i
    a=str(c)+str(expr)+"+"+a
a=a[:-1]
a=a+"=0"
print(a)
rec=open("file1.txt", "w")
rec.write(a)
rec.close()