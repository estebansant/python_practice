import random

def buble_order(list):
    n = len(list)

    for i in range(n):
        for j in range(0, n - i - 1): #O(n) * O(n) = O(n**2)

            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    
    return list        

if __name__ == '__main__':
    list_size = int(input("Which is the list size?"))

    user_list = [random.randint(0, 100) for i in range(list_size)]
    print(user_list)

    ordered_list = buble_order(user_list)
    print(ordered_list)