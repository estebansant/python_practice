with open('/home/estebansant/proyectosProgramacion/python/pyhton-learn/py-population/text.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write("nuevas cosas en este archivo\n")
    file.write("otra linea\n")
    file.write("otra mas\n")