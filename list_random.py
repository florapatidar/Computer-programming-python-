#list of 5 random odd and evening integers
import random
odd_lst=[]
even_lst=[]
for i in range(5):
    odd-lst.append(random.randrange(1,99,2))
print("odd numbers list is:",odd_lst)

for i in range(4):
    even_lst.append(random.randrange(2,100,2))
print("ëven numbers list is",even_lst)

#replace 3e=rd ele of odd lst to even list
odd_lst[2]= even_lst
print("modified odd list is:",odd_lst)

#Faltten te odd list
flat_lst=[]
for i in range(len(odd_lst)):
    if(isinstance(odd_lst[i],list)):
       for j in range(len(odd_lst[i])):
        flat_lst.append(odd_lst[i])
    else:
        flat_lst.append(odd_lst[i])
print("flattened list is",flat_lst)

#sort the list
flat_lst.sort()
print("the sorted list is:",flat_lst)


        
