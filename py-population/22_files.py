file = open('/home/estebansant/proyectosProgramacion/python/pyhton-learn/py-population/text.txt')
# print(file.read())

# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

for line in file:
    print(line)

file.close()

with open('/home/estebansant/proyectosProgramacion/python/pyhton-learn/py-population/text.txt') as file:
    for line in file:
        print(line)