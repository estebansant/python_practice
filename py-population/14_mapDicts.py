items = [
    {
        "product": "camisa",
        "price": 100,
    },
    {
        "product": "pantalones",
        "price": 300
    },
    {
        "product": "pantalones 2",
        "price": 200
    }
]

# Solo quiero tener una lista de precios
prices = list(map(lambda item: item["price"], items)) 

print(prices)

# Quiero agregarle un item a cada objeto (dict), que seria el correspondiente a los impuestos

def add_taxes(item):
    item["taxes"] = item["price"] *.21
    return item

new_items = list(map(add_taxes, items))
print(new_items) 