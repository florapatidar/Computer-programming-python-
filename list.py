#WAP to find out no.of boys and girls in the list
students=['g1','g2',('b1','b2','b3'),'g3' ]
boys=0
girls=0
for i in students:
    if isinstance(i,tuple):
        l=len(i)
        boys+=l
    else:
        girls+=1
print("boys:",boys)
print("girls:",girls)
        

   
