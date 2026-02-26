dict1 = {}
n1 = int(input("How many items in dictionary 1? "))

for i in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

dict2 = {}
n2 = int(input("How many items in dictionary 2? "))

for i in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

dict3 = {}
n3 = int(input("How many items in dictionary 3? "))

for i in range(n3):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict3[key] = value

dict4 = {}
dict4.update(dict1)
dict4.update(dict2)
dict4.update(dict3)

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Dictionary 3:", dict3)
print("Final Dictionary:", dict4)
