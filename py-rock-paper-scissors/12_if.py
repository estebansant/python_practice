if True:
    print("debería ejecutarse")

if False:
    print("Nunca se ejecuta")

pet = input("¿Cuál es tu mascota favorita?")

if pet == "perro":
    print("Excelente!")
elif pet == "gato":
    print("Meh")
elif pet == "pez":
    print("que aburrido")
else:
    print("no tienes mascotas dignas")


stock = int(input("Introduce el stock =>"))

if stock >= 100 and stock <= 1000:
    print("El stock es correcto")
else:
    print("El stock es incorrecto")

number = int(input("Ingrese un número =>"))
result = number % 2
if (result == 0):
    print("par")
else:
    print("impar")
