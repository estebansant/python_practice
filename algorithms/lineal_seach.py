import random

def lineal_search(list, objective):
    match = False

    for element in list: #O(n)
        if element == objective:
            match = True
            break

    return match

if __name__ == '__main__':
    list_size = int(input("Which is the list size?"))
    objective = int(input("Which number do you want to find?"))

    user_list = [random.randint(0, 100) for i in range(list_size)]

    found = lineal_search(user_list, objective)
    print(user_list)
    print(f'Objective element {objective} {"is" if found else "is not"} inside the list')