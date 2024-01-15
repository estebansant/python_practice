import sys
print(sys.path)

import re
text = "Mi numero de telefono es 123 123 4231 8347, el codigo del pais es 54, mi numero de la suerte es 3"

result = re.findall('[0-9]+', text)
print(result)

import time
timestamp = time.time()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)

import collections
numbers = [1,2,1,2,1,1,1,2,3,8,4,3,4,3,5,3,5,6,7,8,4,2,4,5,7,8,0]
counter = collections.Counter(numbers)
print(counter)