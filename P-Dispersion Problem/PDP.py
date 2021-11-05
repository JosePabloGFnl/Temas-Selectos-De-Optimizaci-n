import numpy as np
import math
import random
from operator import attrgetter

#reading the file parameters
fileName = open('outputfile1.txt','r')

main_array = []

class Array:
    def __init__(self, x, y, pos):
        self.x = x
        self.y = y
        self.pos = pos
        self.dist = '-'

    def __repr__(self):
        return '{} : {} : {} : {}'.format(self.x, self.y, self.pos, self.dist)

#converting the parameters intro int variables
def extract_values(line):
    a, b = line.split()
    return int(a), int(b)

pos = 0
with open('outputfile1.txt','r') as file:
    main_array = []

    n, p = extract_values(file.readline())
    for line in file.readlines():
        x, y = extract_values(line)
        pos = pos + 1
        main_array.append(Array(x, y, pos))

#----CONSTRUCTUVE HEURISTIC----
#choosing a random point


initpoint = random.choice(list(main_array))

#for loop used to append the distances
for coord in main_array:
    #calculating the distance between the current point and the one selected
    distance = math.sqrt((initpoint.x - coord.x) ** 2 + (initpoint.y - coord.y) ** 2)
    distance = round(distance)
    # the distance is set to the current object
    coord.dist = distance

main_array.sort(key=attrgetter('dist'), reverse=True)

sum = 0
i=0
result_array=[]

for coord in main_array:
    i=i+1
    sum = sum + coord.dist
    result_array.append(coord.pos)
    if i == p:
        break
print(sum)
print(result_array)

print(main_array)


#creating the output file
file = open("outputfile1LS.txt","w")
file.write(str(n) + " " + str(p) + " " + str(sum) +"\n")

for coord in main_array:

    file.write("" + str(coord.x) + " ")
    file.write("" + str(coord.y) + " ")
    file.write("" + str(coord.pos) + " ")
    file.write("" + str(coord.dist) + "\n")
   
file.close()
