name = "Esteban"
print(name)
lastName = "Santiago"
print(lastName)
myAge = 21
fullName = name + " " + lastName
print(fullName)

quote = "I'm Esteban"
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

# Format
template = "Hola, mi nombre es " + name + "y mi apellido es " + lastName
print("v1", template)

template2 = "Hola, mi nombre es {} y mi apellido es {}".format(name, lastName)
print("v2", template2)

template3 = f"Hola, mi nombre es {name} y mi apellido es {lastName} y mi edad es {myAge}"
print("v3", template3)