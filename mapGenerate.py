import numpy as np
import matplotlib.pyplot as plt

# TODO:
# label the area name with text window
# label the node with letters, if all letter runs out, use "AA, AB etc"
# start thinking the heuristic algorithm and implementation

numRow = input("Enter the number of rows: ")
numColumn = input("Enter the number of columns: ")
numRow = int(numRow)
numColumn = int(numColumn)

node_x = []
node_y = []
area_x = []
area_y = []
edge = []

for y in range(0,numRow+1):
    for x in range(0,numColumn+1):
        node_x.append(1+x*0.2)
        node_y.append(1+y*0.1)

for y in range(0,numRow):
    for x in range(0,numColumn):
        area_x.append(1.1+x*0.2)
        area_y.append(1.05+y*0.1)

for x in range(0,numRow+1):
    edge.append((1 , 1+(numColumn)*0.2))
    edge.append((1+x*0.1 , 1+x*0.1))
    edge.append('r')

for y in range(0,numColumn+1):
    edge.append((1+y*0.2 , 1+y*0.2))
    edge.append((1 , 1+(numRow)*0.1))
    edge.append('r')

plt.title('Assignment_1')

plt.plot(*edge)
plt.scatter(node_x, node_y, marker='o')
plt.scatter(area_x, area_y, marker='o')

plt.show() 



