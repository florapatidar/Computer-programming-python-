s = input("Enter a string: ")

length = len(s)

print("First character:", s[0])
print("Last character:", s[length - 1])

if length % 2 != 0:
    mid = length // 2
    print("Middle character:", s[mid])
else:
    print("No middle character (even length)")
