import numpy as np
import math
import heapq
import time

class Node():
    pass
class Edge():
    pass
class Area():
    pass

class Node():
    def __init__(self, nodeId: str, coorX, coorY):
        # Define the node by Id, x and y corrdinate
        self.nodeId = nodeId
        self.coorX = coorX
        self.coorY = coorY

        # edge list which connected the node
        self.edges: list[Edge] = list()
        # Edge on the node right side, and apply to the rest comment
        self.rightEdge: Edge = None
        self.downEdge: Edge = None
        self.leftEdge: Edge = None
        self.upEdge: Edge = None
        # Previous node, used when final path finding
        self.parentNode: Node = None

        self.gValue = 0
        self.hValue = 0
        self.fValue = 0

class Edge():
    def __init__(self, leftNode: Node, rightNode: Node, leftArea: Area = None, rightArea: Area = None):
        # Each edge have 2 node on left and right side, and 1 or 2 Areas touched
        self.leftNode: Node = leftNode
        self.rightNode: Node = rightNode
        self.leftArea: Area = leftArea
        self.rightArea: Area = rightArea

class Area():
    def __init__(self, areaType: str, coorX, coorY, topRightNode: Node = None, topLeftNode: Node = None, bottomRightNode: Node = None, bottomLeftNode: Node = None):
        # Define the area by its area type such as Qt, PG, Vc, Undefined and area location by coorX and coorY and 4 nodes
        self.areaType = areaType
        self.coorX = coorX
        self.coorY = coorY
        self.topRightNode = topRightNode
        self.topLeftNode = topLeftNode
        self.bottomRightNode = bottomRightNode
        self.bottomLeftNode = bottomLeftNode

class PathMap():
    def __init__(self, numRow = 2, numColumn = 3, quarantineArea:list = ['1' , '6'] , vaccineArea:list = ['2' , '4'], playgroundArea:list = ['3']):
        # The map is defined by # of row and column, with different area type which mentioned above 
        self.numRow = numRow
        self.numColumn = numColumn
        self.quarantineArea = quarantineArea
        self.vaccineArea = vaccineArea
        self.playgroundArea = playgroundArea
        self.map = list(list())
        self.nodes = list(list())
        self.edgeList: list[Edge] = list()

        # Set self.map into numpy array 
        for y in range(0, self.numRow):
            self.map.append(list())
            for x in range(0, self.numColumn):

                for qa in self.quarantineArea:
                    if int(qa) == y * self.numColumn + (x+1):
                        self.map[y].append(Area('Qt', x, y))
                    else:
                        pass
                
                for vc in self.vaccineArea:
                    if int(vc) == y * self.numColumn + (x+1):
                        self.map[y].append(Area('Vc', x, y))
                    else:
                        pass
                
                for pg in self.playgroundArea:
                    if int(pg) == y * self.numColumn + (x+1):
                        self.map[y].append(Area('PG', x, y))
                    else:
                        pass

                var = str(y * self.numColumn + (x+1))
                if var not in self.quarantineArea and var not in self.vaccineArea and var not in self.playgroundArea:
                     self.map[y].append(Area('UN', x, y))

            self.map[y] = np.array(self.map[y])
        self.map = np.array(self.map)


        # Set self.nodes within the map
        count = 0
        node_list = ['A', 'B', 'C', 'D', 'edge', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'node1', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ',
            'BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BK', 'BL', 'BM', 'BN', 'BO', 'BP', 'BQ', 'BR', 'BS', 'BT', 'BU', 'BV', 'BW', 'BX', 'BY', 'BZ',
            'CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG', 'CH', 'CI', 'CJ', 'CK', 'CL', 'CM', 'CN', 'CO', 'CP', 'CQ', 'CR', 'CS', 'CT', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ',
            'DA', 'DB', 'DC', 'DD', 'DE', 'DF', 'DG', 'DH', 'DI', 'DJ', 'DK', 'DL', 'DM', 'DN', 'DO', 'DP', 'DQ', 'DR', 'DS', 'DT', 'DU', 'DV', 'DW', 'DX', 'DY', 'DZ']
        
        for y in range(0, self.numRow+1):
            self.nodes.append(list())
            for x in range(0, self.numColumn+1):
                self.nodes[y].append(Node(node_list[count], x, y))
                count += 1


        # Set self.edgeList within the map
        area : Area
        for x in range(0, self.numRow):
            for y in range(0, self.numColumn):
                area = self.map[x][y]
                area.topLeftNode = self.nodes[x][y]
                area.topRightNode = self.nodes[x][y+1]
                area.bottomLeftNode = self.nodes[x+1][y]
                area.bottomRightNode = self.nodes[x+1][y+1]

                if x == 0:
                    self.edgeList.append(Edge(self.nodes[x][y], self.nodes[x+1][y], None, self.map[x][y]))
                else:
                    self.edgeList.append(Edge(self.nodes[x][y], self.nodes[x+1][y], self.map[x][y-1], self.map[x][y]))
                if y == 0:
                    self.edgeList.append(Edge(self.nodes[x][y], self.nodes[x][y+1], None, self.map[x][y]))
                else:
                    self.edgeList.append(Edge(self.nodes[x][y], self.nodes[x][y+1], self.map[x-1][y], self.map[x][y]))
            self.edgeList.append(Edge(self.nodes[x][self.numColumn], self.nodes[x+1][self.numColumn], self.map[x][self.numColumn-1], None))
        for y in range(self.numColumn):
            self.edgeList.append(Edge(self.nodes[self.numRow][y], self.nodes[self.numRow][y+1], self.map[self.numRow-1][y], None))


    def setNodeEdges(self, node1: Node):
        edge: Edge
        node2: Node
        # for nodeList in self.nodes:
        #     for node1 in nodeList:
        for edge in self.edgeList:
            if node1 == edge.leftNode or node1 == edge.rightNode:
                node1.edges.append(edge)
                if node1 == edge.leftNode:
                    node2 = edge.rightNode
                elif node1 == edge.rightNode:
                    node2 = edge.leftNode
                if node2.coorX-node1.coorX == 1:
                    node1.rightEdge = edge
                elif node2.coorX-node1.coorX == -1:
                    node1.leftEdge = edge
                elif node2.coorY-node1.coorY == 1:
                    node1.downEdge = edge
                elif node2.coorY-node1.coorY == -1:
                    node1.upEdge = edge
        # node = node1
        return node1

    # Assign nodes location (node right, left, up, down edge connection) based on self.edgeList
    def findNeighbor(self, currentNode: Node):
        neighborNode: Node
        edge: Edge
        neighborNodeList = []

        for edge in self.edgeList:
            if currentNode.nodeId == edge.leftNode.nodeId:
                neighborNode = edge.rightNode
                if neighborNode not in neighborNodeList:
                    neighborNodeList.append(neighborNode)

            elif currentNode.nodeId == edge.rightNode.nodeId:
                neighborNode = edge.leftNode
                if neighborNode not in neighborNodeList:
                    neighborNodeList.append(neighborNode)
            else:
                pass
        return neighborNodeList
    

class roleC_AStar():
    def __init__(self, map: PathMap, cost = {'Qt': 0, 'Vc': 2, 'PG': 3, 'UN': 1}):
        # Open list, close list, and final optimal path list
        self.openList : list[Node] = list()
        self.closeList : list[Node] = list()
        self.optPath: list[Node] = list()
        self.map = map
        self.cost = cost
        self.counter = 0
    
    def listPush(self, node: Node, fValue, listName: list):
        # Add new node to list
        self.counter += 1
        heapq.heappush(listName, [fValue, self.counter, node])

    def listPop(self, listName: list):
        # Remove node from list
        [fValue, counter, node] = heapq.heappop(listName)
        return node
    
    def setEdgeCost(self, edge: Edge):
        # Define each edge cost based on the two side areas
        tempCost: float = 0.0
        area1 = edge.leftArea
        area2 = edge.rightArea
        if area1 is not None and area2 is not None:
            tempCost = 0.5 * (self.cost[area2.areaType] + self.cost[area1.areaType])
        elif area1 is None:
            tempCost = self.cost[area2.areaType]
        else:
            tempCost = self.cost[area1.areaType]
        return tempCost
    
    # Get hValue from currentNode to endNode
    def heuristic(self, currentNode: Node, endNode: Node):
        # Create temp variable
        nodeHeuristic = 0.0

        # For heuristic calculation, we use Manhattan distance to define the node
        # Absolute distance from current node to end node by horizontal
        dx = abs(currentNode.coorX - endNode.coorX)
        # Absolute distance from current node to end node by vertical
        dy = abs(currentNode.coorY - endNode.coorY)
        nodeHeuristic = 0.6 * (dx + dy)
        return nodeHeuristic

    # Get edge cost between two connected nodes
    def getCost(self, node1: Node, node2: Node):
        cost = 0.0
        dx = node2.coorX - node1.coorX
        dy = node2.coorY - node1.coorY

        if dx == 0:
            if dy > 0:
                cost += self.setEdgeCost(node1.downEdge)
            elif dy < 0:
                cost += self.setEdgeCost(node1.upEdge)
            else:
                pass
        elif dy == 0:
            if dx > 0:
                cost += self.setEdgeCost(node1.rightEdge)
            elif dx < 0:
                cost += self.setEdgeCost(node1.leftEdge)
            else: 
                pass
        return cost

    def getCostSofar(self, currentNode: Node):
        # pathList = []
        costSoFar = 0.0
        # pathList = self.createPath(currentNode)
        
        # # Total gValues
        # for x in range(len(pathList)-1):
        #     costSoFar += self.getCost(pathList[x], pathList[x+1])
        # return costSoFar
        current: Node = currentNode
        while current is not None:
            # print(current.nodeId)
            if current.parentNode is None:
                break
            else:
                costSoFar += self.getCost(current, current.parentNode)
                current = current.parentNode
        return costSoFar

    def createPath(self, currentNode: Node):
        path = []
        current: Node = currentNode
        while current is not None:
            path.append(currentNode)
            current = current.parentNode
        return path[::-1]  # Return reversed path

    def pathFind(self, startArea: Area, endArea: Area):
        # Define start, current, end node
        startNode: Node = startArea.topRightNode
        currentNode: Node = startNode
        endNode: Node = endArea.topRightNode

        # Set the f value of current node which is start node now
        currentNode.fValue = self.heuristic(startNode, endNode)
        # Add start node into openlist
        self.listPush(currentNode, currentNode.fValue, self.openList)

        # # Pop start node from openlist and push it into closelist
        # self.listPop(self.openList)
        # self.listPush(currentNode, currentNode.fValue, self.closeList)
        
        # # Push start node neighbors to openlist
        # for x in self.map.findNeighbor(currentNode):
        #     tempCurrent: Node = self.map.setNodeEdges(currentNode)
        #     self.listPush(x, self.getCost(tempCurrent, x) + self.heuristic(x, endNode), self.openList)

        while len(self.openList) > 0:
            # Pop the lowest fValue node
            currentNode = self.listPop(self.openList)
            tempCurrent: Node = self.map.setNodeEdges(currentNode)
            # print(self.openList)


            if tempCurrent == endNode:
                print("Path found. ")
                print(self.createPath(tempCurrent))
                break

            else:  
                self.listPush(tempCurrent, tempCurrent.fValue, self.closeList)
                print(self.closeList[0][2].nodeId)

                # Loop each neighbor node which connected with current node
                for x in self.map.findNeighbor(tempCurrent):
                    print(x.nodeId)
                    # print(x.coorX)
                    # print(x.coorY)
                    time.sleep(0.1)
                    tempX: Node = self.map.setNodeEdges(x)

                    # print(tempX.nodeId)
                    # print(tempX.rightEdge)
                    # print(tempX.leftEdge)
                    # print(tempX.upEdge)
                    # print(tempX.downEdge)
                    # print(self.setEdgeCost(tempX.upEdge))

                    # If new neighbor not is in the close list
                    for closeListIndex in range(len(self.closeList)):
                    # if tempX in self.closeList:
                    #     continue
                        print(1)
                        if tempX == self.closeList[closeListIndex][2]:
                            continue

                    if tempX not in self.openList:
                        # tentative_gValue = self.getCostSofar(tempCurrent) + self.getCost(tempCurrent, x)
                        tempX.parentNode = tempCurrent
                        tempX.gValue = self.getCostSofar(tempCurrent) + self.getCost(tempCurrent, tempX)

                        # print(self.getCostSofar(tempCurrent))
                        # print(self.getCost(tempCurrent, tempX))

                        # tempX.gValue = self.getCost(tempCurrent, tempX)
                        tempX.hValue = self.heuristic(tempX, endNode)
                        tempX.fValue = tempX.gValue + tempX.hValue     
                        self.listPush(tempX, tempX.fValue, self.openList)
                        print(" ---- " + tempX.nodeId)
                    
        # self.optPath.append(self.createPath(x))
        # print(self.optPath)


