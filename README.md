# ENPM661_Proj2
Dijkstra implementation for Point and Rigid Robot

The two main files are dijkstra_point.py and dijkstra_rigid.py

## Installation
```bash
pip install opencv-contrib-python
pip install numpy
```

## Usage for Dijkstra Point
```python
python dijkstra_point.py
```
The user will then be prompted to enter the start and end node carteisian coordiantes line by line.
Two screens will appear. The first will show all the nodes that the program checks. The second will come when the program finishes and will display the optimal path to the goal.

## Usage for Dijkstra Rigid
```python
python dijkstra_ridig.py
```
The user will be prompted to enter the start and end node cartesian coordinates, radius of the rigid robot, and clearance. The same two screens will appear here. The clearance and radius are adjusted for by increasing the size of the obstacles, so the visual map may not show the true shape of the obstacle.

## Execution time for the Algorithm (Point Robot)
Start position: 5, 5  
Goal position: 295 195  
Total time to run dijkstra: 4.436329 seconds  