# CRUD
# Create
numbers = [1, 2, 3, 4, 5]
# Read
print(numbers[1])
# Update
numbers[-1] = 10
print(numbers)

# Add
numbers.append(700)
print(numbers)

# Insert, receives 2 values. Position and value
numbers.insert(0, "hola")
print(numbers)

numbers.insert(3, "cambio")
print(numbers)

tasks = ["todo 1", "todo 2", "todo 3"]
newList = numbers + tasks
print(newList)

# Element position
indexTodo = newList.index("todo 2")
newList[indexTodo] = "todo changed"
print(newList)

# Delete with remove
newList.remove("todo 1")
print(newList)

# Delete with pop
newList.pop()
print(newList)

newList.pop(0)
print(newList)

# Reverse the array
newList.reverse()
print(newList)

# Ordernar arrays
numbers_a = [1, 4, 6, 3]
numbers_a.sort()
print(numbers_a)
text_a = ["re", "ab", "ed"]
text_a.sort()
print(text_a)