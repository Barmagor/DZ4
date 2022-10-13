My_list=[1,2,3,2,1,5,2,6,2]
temp=[]
for j in My_list:
    if j not in temp:
        temp.append(j)
My_list=temp
print(My_list)