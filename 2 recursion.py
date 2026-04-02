def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary(n // 2) + str(n % 2)

num = int(input("Enter a positive integer: "))

if num < 0:
    print("Please enter a positive integer.")
else:
    binary = decimal_to_binary(num)
    print(f"Binary equivalent of {num} is: {binary}")
