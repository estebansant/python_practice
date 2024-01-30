import random

def binary_search(list, begin, end, objective):
    print(f'searching for {objective} between {list[begin]} and {list[end - 1]}')
    if begin > end:
        return False
    
    mid = (begin + end) // 2

    if list[mid] == objective:
        return True
    elif list[mid] < objective:
        return binary_search(list, mid + 1, end, objective)
    else:
        return binary_search(list, begin, mid - 1, objective) 

if __name__ == '__main__':
    list_size = int(input("Which is the list size?"))
    objective = int(input("Which number do you want to find?"))

    user_list = sorted([random.randint(0, 100) for i in range(list_size)])

    found = binary_search(user_list, 0, len(user_list), objective)
    print(user_list)
    print(f'Objective element {objective} {"is" if found else "is not"} inside the list')