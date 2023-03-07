print("Welcome to prime number finder.")

number = int(input("Type an integer higher than 0 to see if it is prime number or not: "))
divisible_by = []

def pf(n = number):
    divisible_count = 0
    for c in range(1, n+1):
        if n % c == 0:
            divisible_count += 1
            divisible_by.append(c)
    
    if divisible_count == 2:
        print("This number is prime.")
    
    else:
        print("This number is not prime.")

    print(f"{n} is divisible by {divisible_by}")

pf()