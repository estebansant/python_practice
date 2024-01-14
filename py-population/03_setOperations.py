# Union
setA = {"col", "mex", "bol"}
setB = {"arg", "bol"}

setC = setA.union(setB)
print(setC)

print(setA | setB)

setD = setA | setB
print(setD)

# Intersection

setC = setA.intersection(setB)
setD = setA & setB
print(setC)
print(setD)

# Difference
setC = setA.difference(setB)
print(setC)
setD = setA - setB
print(setD)

# Symmetric Difference
setC = setA.symmetric_difference(setB)
print(setC)
setD = setA ^ setB
print(setD)
