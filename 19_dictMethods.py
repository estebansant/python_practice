person = {
    "name": "Esteban",
    "last_name": "Santiago",
    "langs": ["python", "javascript"],
    "age": 21
}

print(person)

person["name"] = "Thiago"
person["age"] += 12
person["langs"].append("go")
print(person)

del person["last_name"]
person.pop("age")


print("ITEMS")
print(person.items())

print("KEYS")
print(person.keys())

print("VALUES")
print(person.values())