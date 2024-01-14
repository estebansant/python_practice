import random
countries = ["col", "mex", "arg"]

populationV2 = { country: random.randint(1, 100) for country in countries}

print(populationV2)

result = {country: population for (country, population) in populationV2.items() if population > 20}
print(result)

text = "Hola, soy Esteban"
unique = {c: text.count(c) for c in text if c in "aeiou"}
print(unique)