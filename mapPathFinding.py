import numpy as np

            
class Node():
    pass
class Edge():
    pass
class Area():
    pass

class Node():
    def __init__(self, nodeId: str, coorX, coorY):
        self.id = nodeId
        self.coorX = coorX
        self.coorY = coorY

        # Edge on the node right side, and apply to the rest comment
        self.rightEdge: Edge = None
        self.downEdge: Edge = None
        self.leftEdge: Edge = None
        self.upEdge: Edge = None
        # Previous node, used when final path found
        self.lastNode: Node = None
        # Next node
        self.nexNodet: Node = None

class Edge():
    def __init__(self, leftNode: Node, rightNode: Node, leftArea: Area = None, rightArea: Area = None):
        # Each edge have 2 node on left and right side, and 1 or 2 Areas touched
        self.leftNode: Node = leftNode
        self.rightNode: Node = rightNode
        self.leftArea: Area = leftArea
        self.rightArea: Area = rightArea

class Area():
    def __init__(self, areaType: str, coorX, coorY, topRightNode: Node = None, topLeftNode: Node = None, bottomRightNode: Node = None, bottomLeftNode: Node = None):
        # Each area has 4 nodes and it defined by the area type such as Qt, PG, Vc, Undefined and area location by coorX and coorY.
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

        # Set area name for the map into numpy array 
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

        
        # Set node name within the maps
        count = 0
        node_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ',
            'BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BK', 'BL', 'BM', 'BN', 'BO', 'BP', 'BQ', 'BR', 'BS', 'BT', 'BU', 'BV', 'BW', 'BX', 'BY', 'BZ',
            'CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG', 'CH', 'CI', 'CJ', 'CK', 'CL', 'CM', 'CN', 'CO', 'CP', 'CQ', 'CR', 'CS', 'CT', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ',
            'DA', 'DB', 'DC', 'DD', 'DE', 'DF', 'DG', 'DH', 'DI', 'DJ', 'DK', 'DL', 'DM', 'DN', 'DO', 'DP', 'DQ', 'DR', 'DS', 'DT', 'DU', 'DV', 'DW', 'DX', 'DY', 'DZ']
        
        for y in range(0, self.numRow+1):
            self.nodes.append(list())
            for x in range(0, self.numColumn+1):
                self.nodes[y].append(Node(node_list[count], x, y))
                count += 1

        # Set node with areas on the map by edge list
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
        # print(self.edgeList)


x = PathMap()
