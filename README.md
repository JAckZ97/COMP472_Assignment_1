# COMP472_Assignment_1

### Running requirement 
```
pip install numpy
pip install matplotlib

python Assignment1.py   # To start the program
```

### Task:
- Create a heuristic search algorithm to find the optimal paths between any located point on the map.

### Desgin:
#### Pre-request:
- Four types of places on the maps, quarantine, vaccine, play ground, and undefined.
- Design for Role C (Covid-19 confirmed patients).
- Role C head to the quarantine place only.
- Role C only allow to move on the edges of the cell.
- Role C are not allowed to move on the edge between two play ground.
- Role C starting point can be anywhere on the map, but if it's not top right corner of cell, it will beconsider as top right.
- Role C ending point will be the closed quarantine cell top right corner

#### Program cases:
```
Starting point in quarantine cell (include 4 nodes and 4 edges):
    print("Covid-19 confirmed patient is in the quaratine grid right now. ").
    print("No path is found, Please try again! ").

Starting point in other areas except quarantine cell |and| ending point in quarantine cell:
    1. go to top right cornor of starting point cell. (Consider the closest one in terms of geometric distance, ref: https://moodle.concordia.ca/moodle/mod/forum/discuss.php?d=746188)
    2. find top right cornor of closest quarantine area.
    3. find the optimal path from starting point to ending point.

Starting / ending point both are in other areas except quarantine cell (include 4 nodes and 4 edges):
    print("Ending point is not in quarantine grid, which is not designed for Role C. ")
```

#### Design of heuristic algorithm
~~TODO:~~ 
- Defining h(n)
    - How to compare current node with destination node by a number
    - Calculate the f(n) by g(n) + h(n)
    - Make sure use traverse back method
- Classify the node and edge with areas
- Find the range for starting node and ending node
