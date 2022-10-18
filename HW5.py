
def get_degree_of_number(num):
    return int((num.split("*x**"))[1])

def get_coefficient_of_number(num):
    return int((num.split("*x**"))[0])


a="87*x**21+55*x**3+39*x**2+97*x**1+221*x**0"
b="3*x**5+16*x**4+87*x**3+46*x**2+20*x**1+821*x**0"

mas1 = a.split("+")
mas2 = b.split("+")
print(mas1)
print(mas2)

result = [0]*(max(int((mas1[0].split("*x**"))[1]),int((mas2[0].split("*x**"))[1]))+1)

print(result)

for num1 in mas1:
    result[get_degree_of_number(num1)] += get_coefficient_of_number(num1)

for num2 in mas2:
    result[get_degree_of_number(num2)] += get_coefficient_of_number(num2)

print(result)

for i in range(len(result)-1,0,-1):
    if result[i] !=0:
        print(f"{result[i]}*x**{i}",end="+")

if result[0] !=0:
    print(f"{result[-1]}*x**{0}")
