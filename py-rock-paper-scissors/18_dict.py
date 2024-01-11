my_dict = {}
print(type(my_dict))

my_dict = {
    "name": "Esteban",
    "last_name": "Santiago",
    "age": 21
}

print(my_dict)
print(len(my_dict))

print(my_dict["age"])
print(my_dict["last_name"])
print(my_dict.get("value"))

print('age' in my_dict)
print('value' in my_dict)