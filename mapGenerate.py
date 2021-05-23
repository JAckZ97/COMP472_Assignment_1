import numpy as np
import matplotlib.pyplot as plt

# TODO:
# start thinking the heuristic algorithm and implementation
# map, zones, coners, etc.

# # Instruction for defining area by cell number
# print("Define each areas by cells number. Starting with number ")
# print("1 from top left, and ending with number n from bottom right. ")
# print("Exampe as 2 row, 3 columns: ")
# print(".___.____.____.")
# print("| 1 || 2 || 3 |")
# print(".___.____.____.")
# print("| 4 || 5 || 6 |")
# print(".___.____.____.")

# # Enter row number and column number to generate maps
# numRow = input("Enter the number of rows: ")
# numColumn = input("Enter the number of columns: ")
# numRow = int(numRow)
# numColumn = int(numColumn)
numRow = 2
numColumn = 3

# # Enter cell number to define the areas 
# print("After pick the defined area (quarantine, vaccine, play ground), ")
# print("and the rest area will be undefined area. ")
# quarantineArea = input("Define quarantine place by cell number: ")
# vaccineArea = input("Define vaccine spot by cell number: ")
# playgroundArea = input("Define play ground by cell number: ")
# undefinedArea = []
quarantineArea = ['1' , '6']
vaccineArea = ['2' , '4']
playgroundArea = ['3']

# -------------- map generating --------------
node_x = []
node_y = []
area_x = []
area_y = []
edge = []

# Program is designed for maximum of 10*10 map size; therefore, we create a node list with 26*5 = 130 > 11*11 = 121
node_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ',
            'BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BK', 'BL', 'BM', 'BN', 'BO', 'BP', 'BQ', 'BR', 'BS', 'BT', 'BU', 'BV', 'BW', 'BX', 'BY', 'BZ',
            'CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG', 'CH', 'CI', 'CJ', 'CK', 'CL', 'CM', 'CN', 'CO', 'CP', 'CQ', 'CR', 'CS', 'CT', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ',
            'DA', 'DB', 'DC', 'DD', 'DE', 'DF', 'DG', 'DH', 'DI', 'DJ', 'DK', 'DL', 'DM', 'DN', 'DO', 'DP', 'DQ', 'DR', 'DS', 'DT', 'DU', 'DV', 'DW', 'DX', 'DY', 'DZ']

# Qt as quarantine 
# Vc as vaccine 
# PG as play ground
area_list = ['Qt', 'Vc', 'PG']

# Create node coordinate in list
for y in range(0,numRow+1):
    for x in range(0,numColumn+1):
        node_x.append(1+x*0.2)
        node_y.append(1+y*0.1)

# Create area coordinate in list
for y in range(0,numRow):
    for x in range(0,numColumn):
        area_x.append(1.1+x*0.2)
        area_y.append(1.05+y*0.1)

# Create each edge start and end point coordinate in list
for x in range(0,numRow+1):
    edge.append((1 , 1+(numColumn)*0.2))
    edge.append((1+x*0.1 , 1+x*0.1))
    edge.append('r')

for y in range(0,numColumn+1):
    edge.append((1+y*0.2 , 1+y*0.2))
    edge.append((1 , 1+(numRow)*0.1))
    edge.append('r')

# Plot the map with edges and nodes
plt.title('Assignment_1')
plt.plot(*edge)
plt.scatter(node_x, node_y, marker='o')
plt.scatter(area_x, area_y, marker='o')

# Label the name for each nodes of the map
count = 0
for y in range(numRow+1, 0, -1):
    for x in range(0, numColumn+1):
        plt.text(1+x*0.2, 1+(y-1)*0.1, node_list[count], fontsize=14)
        count += 1

# Label the name for each areas of the map
temp = []
var = ""
for a in range(0,numRow):
    temp.append(a)

for y in range(numRow, 0, -1):
    for x in range(0, numColumn):

        # Label quarantine areas
        for qa in quarantineArea:
            if int(qa) == int(temp[-y]) * numColumn + (x+1):
                plt.text(1.1+x*0.2, 1.05+(y-1)*0.1, area_list[0], fontsize=14)
            else:
                pass
        
        # Label vaccine areas
        for vc in vaccineArea:
            if int(vc) == int(temp[-y]) * numColumn + (x+1):
                plt.text(1.1+x*0.2, 1.05+(y-1)*0.1, area_list[1], fontsize=14)
            else:
                pass
        
        # Label play ground areas
        for pg in playgroundArea:
            if int(pg) == int(temp[-y]) * numColumn + (x+1):
                plt.text(1.1+x*0.2, 1.05+(y-1)*0.1, area_list[2], fontsize=14)
            else:
                pass
        
        # Label undefined areas with cell number
        var = str(int(temp[-y]) * numColumn + (x+1))
        if var not in quarantineArea and var not in vaccineArea and var not in playgroundArea:
            plt.text(1.1+x*0.2, 1.05+(y-1)*0.1, str(int(temp[-y]) * numColumn + (x+1)), fontsize=14)
        

plt.show() 
# --------------------------------------------

