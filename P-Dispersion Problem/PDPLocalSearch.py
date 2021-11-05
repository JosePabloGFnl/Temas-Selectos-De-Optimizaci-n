import math
from operator import attrgetter

#reading the file parameters
fileName = 'outputfile1LS.txt'

main_array = []

class Array:
    def __init__(self, x, y, pos, dist):
        self.x = x
        self.y = y
        self.pos = pos
        self.dist = dist
        self.newdist = '-'

    def __repr__(self):
        return '{} : {} : {} : {} : {}'.format(self.x, self.y, self.pos, self.dist, self.newdist)

#converting the parameters intro int variables
def extract_values(line):
    values = line.split()

    if(len(values) == 3):
        return int(values[0]), int(values[1]), int(values[2])  

    else:
        return int(values[0]), int(values[1]), int(values[2]), int(values[3])

with open(fileName,'r') as file:
    main_array = []

    n, p, sum = extract_values(file.readline())
    for line in file.readlines():
        x, y, pos, dist = extract_values(line)
        main_array.append(Array(x, y, pos, dist))

#----LOCAL SEARCH MOVE----
counter=0
for coord in main_array:
    #calculating the distance between the current point and the one selected
    distance = math.sqrt((main_array[p-1].x - coord.x) ** 2 + (main_array[p-1].y - coord.y) ** 2)
    distance = round(distance)
    coord.newdist = distance
    if(counter<=(p-1)):
        coord.newdist=0
    # the distance is set to the current object
    counter=counter+1

newsum = sum - main_array[p-1].dist
main_array.sort(key=attrgetter('newdist'), reverse=True)

newsum = (sum + main_array[0].newdist)


print(newsum)

print(main_array)