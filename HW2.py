def simple_multi(num): 
    list=[]
    i=2
    while num != 1:
        if num % i == 0:
            list.append(i)
            num /= i
        else:
            i += 1
    return list

print("Введите число: ") 
num = int(input())
print(simple_multi(num), end=" ")