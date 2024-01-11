text = "Ella sabe Python"
print(text[0])
print(text[1])
# print(text[999])

print(text[-1])

size = len(text) - 1
print("size =>", size)
print(text[size])

# slicing

print(text[0:5])
print(text[10:16])
print(text[:10])
print(text[0:10])
print(text[5:])
print(text[:])

# Saltos
print(text[10:16:1])
print(text[10:16:2])
print(text[::2])