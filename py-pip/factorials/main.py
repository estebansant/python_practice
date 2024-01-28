def factorial(n):
    """
        Caculate the factorial of n

        n int > 0
        returns n!
    """

    print(n)
    # Base case
    if n == 1:
        return 1
    
    # Factorial case
    return n * factorial(n-1)

n = int(input("Enter an int number: "))
print(factorial(n))

# Python breaks when n >= 1000