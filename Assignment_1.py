from mapGenerate import *

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
quarantineArea = ['1' , '6']
vaccineArea = ['2' , '4']
playgroundArea = ['3']


x = Map(numRow, numColumn, quarantineArea, vaccineArea, playgroundArea)
x.drawMap()