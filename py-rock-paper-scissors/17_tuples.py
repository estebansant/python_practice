numbers = (1, 2, 3, 5)
strings = ("nico", "nutria", "zule", "nico", "nico")
print(numbers)
print("0 =>", numbers[0])
print("-1 =>", numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

print(strings.index("zule"))
print(strings.count("nico"))

myList = list(strings)
print(myList)
print(type(myList))

myList[1] = "juli"
print(myList)

myTuple = tuple(myList)
print(myTuple)
print(type(myTuple))
