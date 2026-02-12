import random
lst=[random.randint(1,30) for i in range(50)]
print("the list is:",lst)

#remove duplicate entries from list
new_list=[]
for i in lst:
    if i not in new_list:
        new_list.apppend(i)

print("unique lis is:",new_list)
