def get_population():
    keys = ["col", "ven"]
    values = [51, 30]
    return keys, values

def population_by_country(data, country):
    result = list(filter(lambda item: item["Country"] == country, data))
    return result
