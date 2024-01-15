def increment(x):
    return x + 1

incrementV2 = lambda x : x + 1 

def high_ord_func(x, func):
    return x + func(x)

high_ord_funcV2 = lambda x, func : x + func(x)

result = high_ord_func(2, increment)

print(result)

result = high_ord_funcV2(2, increment)

print(result)