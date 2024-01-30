import random

def merge_order(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        print(left, '*' *5, right)

        # Recursive calle for each half
        merge_order(left)
        merge_order(right)

        # Iterators to iterate both sublists
        i = 0
        j = 0
        # Iterator for main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
        print(f'left {left}, right {right}')
        print(list)
        print('-' * 5)

    return list 

if __name__ == '__main__':
    list_size = int(input("Which is the list size?"))

    user_list = [random.randint(0, 100) for i in range(list_size)]
    print(user_list)
    print("-" * 20)

    ordered_list = merge_order(user_list)
    print(ordered_list)