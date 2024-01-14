# dict = {}
# for i in range(1, 6):
#     dict[i] = i*2

# print(dict)

# dictV2 = { i: i * 2 for i in range(1,6)}
# print(dictV2)

# Example 2
import random
countries = ["col", "mex", "arg"]
population = {}
for country in countries:
    population[country] = random.randint(1, 100)

print(population)

populationV2 = { country: random.randint(1, 100) for country in countries}

print(populationV2)

# Example 3
names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

print(list(zip(names, ages)))

newDict = {name: age for (name, age) in zip(names,ages)}
print(newDict)