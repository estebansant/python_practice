x = 3.3
y = 1.1 + 2.2
print(x)
print(y)

print(x == y)

# Comparacion con strings
y_string = format(y, ".2g")
print("string =>", y_string)
print(y_string == str(x))

print("*" * 10)
# Comparacion matematica

print(y, x)
tolerance = 0.00001
print(abs(y-x) < tolerance)