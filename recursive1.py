#if +ve integer entered through keyword,write recursive function to obtain prime factors of the number
def prime_factors(n, i=2):
    if n <= 1:
        return []
    if n % i == 0:
        return [i] + prime_factors(n // i, i)
    else:
        return prime_factors(n, i + 1)

num = int(input("Enter a positive integer: "))
if num > 0:
    factors = prime_factors(num)
    print(f"Prime factors of {num} are: {factors}")
else:
    print("Please enter a positive integer.")

