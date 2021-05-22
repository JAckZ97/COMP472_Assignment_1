import numpy as np
import matplotlib.pyplot as plt

# TODO:
 
numRow = input("Enter the number of rows: ")
numColumn = input("Enter the number of columns: ")
numRow = int(numRow)
numColumn = int(numColumn)
# numRow = 2
# numColumn = 3

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

# print(edge)

# plt.title('Assignment_1')

# node_x = [1, 1.2, 1.4, 1.6, 1, 1.2, 1.4, 1.6, 1, 1.2, 1.4, 1.6]
# node_y = [1, 1, 1, 1, 1.1, 1.1, 1.1, 1.1, 1.2, 1.2, 1.2, 1.2]

# area_x = [1.1, 1.3, 1.5, 1.1, 1.3, 1.5]
# area_y = [1.05, 1.05, 1.05, 1.15, 1.15, 1.15]

# edge=[(1, 1.6), (1, 1),'r', (1, 1.6), (1.1, 1.1),'r', (1, 1.6), (1.2, 1.2),'r', 
#     (1, 1), (1, 1.2),'r', (1.2, 1.2), (1, 1.2),'r', (1.4, 1.4), (1, 1.2),'r', (1.6, 1.6), (1, 1.2),'r']

plt.plot(*edge)
plt.scatter(node_x, node_y, marker='o')
plt.scatter(area_x, area_y, marker='o')

plt.show() 



