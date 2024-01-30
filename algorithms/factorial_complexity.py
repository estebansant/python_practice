import time

def factorial(n):
    response = 1

    while n > 1:
        response *= n
        n -= 1

    return response

def factorial_recursive(n):
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

if __name__ == '__main__':
    n=200000

    begin = time.time()
    factorial(n)
    end = time.time()
    print(end - begin)

    begin = time.time()
    factorial_recursive(n)
    end = time.time()
    print(end - begin)