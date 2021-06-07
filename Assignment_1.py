from mapGenerate import *
from mapPathFinding import *

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
# quarantineArea = input("Define quarantine place by cell number (Enter separated by space): ")
# vaccineArea = input("Define vaccine spot by cell number(Enter separated by space): ")
# playgroundArea = input("Define play ground by cell number(Enter separated by space): ")
# # Split the input into a list
# quarantineAreaSplit: list = quarantineArea.split()
# vaccineAreaSplit: list = vaccineArea.split()
# playgroundAreaSplit: list = playgroundArea.split()
quarantineAreaSplit = ['1' , '6']
vaccineAreaSplit = ['2' , '4']
playgroundAreaSplit = ['3']

# # -------------- map generating --------------
# x = Map(numRow, numColumn, quarantineAreaSplit, vaccineAreaSplit, playgroundAreaSplit)
# x.drawMap()
# # --------------------------------------------

def main():
    map = PathMap(numRow, numColumn, quarantineAreaSplit, vaccineAreaSplit, playgroundAreaSplit)
    roleC = roleC_AStar(map)
    area1 : Area = map.map[0][2]
    area2 : Area = map.map[0][0]
    # # area2 : Area = map.map[3][4]

    roleC.pathFind(area1, area2)
    print(roleC.createPath(area2.topRightNode))

    
main()
