text = "Ella sabe programar en Python"
print("JavaScript" in text)
print("Python" in text)

if "Python" in text:
    print("Bien hecho!")
else:
    print("Es válido")

size = len(text)
print(size)

print("PRUEBAS MÉTODOS")
print(text)
print(text.upper())
print(text.lower())
print(text.count("a"))
print(text.swapcase())
print(text.startswith("Ella"))
print(text.endswith("JavaScript"))
print(text.replace("Python", "Go"))

text_2 = "este es un título"

print(text_2)
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())
print("234".isdigit())
print(text.capitalize())
