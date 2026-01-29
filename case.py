#convert cases
s = input("Enter a string: ")
choice = input("Choose mode (lower / upper / toggle): ")

result = ""

for ch in s:
    if choice == "lower":
        if 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch

    elif choice == "upper":
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch

    elif choice == "toggle":
        if 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        elif 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch

    else:
        result = "Invalid choice"
        break

print("Result:", result)
