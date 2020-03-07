import os
import cv2
import copy
import numpy as np
import heapq
import time

import sys
sys.dont_write_bytecode = True

import actions
import obstacles
import node
import utils
import dijkstra


##
## The main function
##
def main():
	start_time = time.clock()
	input_map = obstacles.getMap(radius=0, visualize=False)
	print "Time to build the map:", time.clock() - start_time, "seconds"

	# User input for the start state
	start_r = input_map.shape[0] - int(input("Enter the start row: "))
	start_c = int(input("Enter the start col: "))
	if (start_r < 0 or start_c < 0 or start_r >= input_map.shape[0] or start_c >= input_map.shape[1] or obstacles.insideObstacle(start_r, start_c, radius=0)):
		print("ERROR: This start state is invalid. Possible issues can be that the start position lies outside the map region or within the obstacle. Please try a different starting position.")
		return 

	# User input for the goal state
	goal_r = input_map.shape[0] - int(input("Enter the goal row: "))
	goal_c = int(input("Enter the goal col: "))
	if (goal_r < 0 or goal_c < 0 or goal_r >= input_map.shape[0] or goal_c >= input_map.shape[1] or obstacles.insideObstacle(goal_r, goal_c, radius=0)):
		print("ERROR: This goal state is invalid. Possible issues can be that the goal position lies outside the map region or within the obstacle. Please try a different goal position.")
		return 

	start_time = time.clock()
	# Get the path after running the dijkstra algorithm 
	path = dijkstra.getDijkstraPath(input_map, (start_r, start_c), (goal_r, goal_c), original_map=input_map)
	print "Time to run Dijkstra:", time.clock() - start_time, "seconds"

	# Visualize the path on the input_map
	for i in path:
		input_map[i.current_coords] = 255
	cv2.imshow("Map", input_map)

	 #if 'q' is pressed then quit visualization
	while(1):
		key = cv2.waitKey(1) & 0xFF
		if key == 27 or key == ord("q"):
		    break

if __name__ == '__main__':
	main()
