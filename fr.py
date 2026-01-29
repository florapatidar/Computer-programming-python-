s = input("Enter a string: ")

# Forward traversal
i = 0
print("Forward order:")
while i < len(s):
    print(s[i], end=" ")
    i += 1

# Reverse traversal
i = len(s) - 1
print("\nReverse order:")
while i >= 0:
    print(s[i], end=" ")
    i -= 1
