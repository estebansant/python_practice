# for element in range(1, 21):
#     print(element)

myList = [23, 45, 67, 89, 43]

for i in myList:
    print(i)

myTuple = ('nico', 'juli', 'santi')

for i in myTuple:
    print(i)

person = {
    "name": "Esteban",
    "last_name": "Santiago",
    "age": 21
}

for key in person:
    print(key, "=>", person[key])

for key, value in person.items():
    print(key, "=>", value)

people = [
    {
        "name": "Esteban",
        "last_name": "Santiago",
        "age": 21
    },
    {
        "name": "Jhon",
        "last_name": "Doe",
        "age": 45
    },
    {
        "name": "Will",
        "last_name": "Smith",
        "age": 55
    },
]

for person in people:
    print("name =>", person["name"])