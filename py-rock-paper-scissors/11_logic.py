# and
print("AND")
print("True and True =>", True and True)
print("True and False =>", True and False)
print("False and True =>", False and True)
print("False and False =>", False and False)

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)
print(10 > 5 and 5 > 3 and 3 > 1)

stock = input("Ingrese el número de stock =>")
stock = int(stock)

print(stock >= 100 and stock <= 1000)

# Or
print("OR")
print("True and True =>", True or True)
print("True and False =>", True or False)
print("False and True =>", False or True)
print("False and False =>", False or False)

role = input("Digita el rol =>")
print(role == "admin" or role == "seller")

# Not
print("NOT")
print(not True or not True)
print(not False)

print("True and True =>", not (True and True))
print("True and False =>", not (True and False))
print("False and True =>", not (False and True))
print("False and False =>", not (False and False))

stock = input("Ingrese el número de stock =>")
stock = int(stock)

print(not (stock >= 100 and stock <= 1000))