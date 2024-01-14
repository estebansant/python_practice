numbers = []
for i in range(1,11):
    numbers.append(i * 2)

print(numbers)

numbersV2 = [i * 2 for i in range(1, 11)]
print(numbersV2)

cicle = [i for i in range(1,101) if i % 2 == 0]

print(cicle)