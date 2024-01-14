setCountries = {"col", "mex", "ven"}

size = len(setCountries)
print(size)

print('col' in setCountries)
print('arg' in setCountries)

# add
setCountries.add("arg")
print(setCountries)
print('arg' in setCountries)

# update
setCountries.update({"ecua", "chi", "arg"})
print(setCountries)

# remove
setCountries.remove("chi")
print(setCountries)
setCountries.discard("ch")
setCountries.clear()
print(setCountries)
