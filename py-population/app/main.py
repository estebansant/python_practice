import utils

data = [
        {
            "Country": "Colombia",
            "Population": 51
        },
        {
            "Country": "Venezuela",
            "Population": 30
        },
    ]

def run():
    keys, values = utils.get_population()
    print(keys, values)

    country = input("Escribe un país =>").capitalize()

    result = utils.population_by_country(data, country)
    print(result)

if __name__ == "__main__":
    run()