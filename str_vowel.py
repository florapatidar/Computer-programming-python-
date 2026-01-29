#count vowels
s=input("enter a string:")
x=0
vow=['a','e','i','o','u']
for  i in s:
    if i in vow:
        x+=1
print ("total number of vowels:",x)
