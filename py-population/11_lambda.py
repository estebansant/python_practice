def increment(x):
    return x + 1

incrementV2 = lambda x : x + 1

result = increment(10)
print(result)

result = incrementV2(20)
print(result)

fullName = lambda name, lastName : f"Full Name is {name.title()} {lastName.title()}"

text = fullName('Esteban', 'santiago pizzani')
print(text)