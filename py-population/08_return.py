def sum_with_range(min, max):
    print(min, max)
    sum = 0 
    for x in range(min, max):
        sum += x
    return sum

result1 = sum_with_range(1, 10)
result2 = sum_with_range(result1, result1 + 30)
result3 = sum_with_range(result2, result2 + 100)

print(result1)
print(result2)
print(result3)