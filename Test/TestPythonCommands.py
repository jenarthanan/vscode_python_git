import math
import random
Alphabets = [chr(i) for i in range(65, 91)]
# print(str.join('', Alphabets))

listTable = [[0] * 10 for i in range(10)]

for i in range(10):

    for j in range(10):
        listTable[i][j] = "{} : {}".format(i, j)

for i in range(10):

    for j in range(10):
        print(listTable[i][j], end=" || ")
    print()
