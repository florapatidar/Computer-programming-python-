import random

def q2_list():
    lst=[random.randint(1,50) for x in range(20)]
    print(lst)
    n=int(input("enter a number:"))
    if lst.count(n)>1:
        for i,v in enumerate(lst):
            if v== n:
                print(i)
            else:
                print(n,"is not found")
q2_list()
