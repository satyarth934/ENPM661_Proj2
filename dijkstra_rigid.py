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


def main():

	radius = int(input("Enter the robot radius: "))
	clearance = int(input("Enter the clearance: "))

	input_map = obstacles.getMap(radius=(radius + clearance), visualize=False)
	orign_map = obstacles.getMap(radius=0, visualize=False)

	# User input for the start state
	start_c, start_r = map(int, raw_input("Enter starting coordinates (x y): ").split())
	start_r = input_map.shape[0] - start_r
	if (start_r < 0 or start_c < 0 or start_r >= input_map.shape[0] or start_c >= input_map.shape[1] or obstacles.insideObstacle(start_r, start_c, radius=(radius + clearance))):
		print("ERROR: This start state is invalid for the given robot size and clearance distance. Possible issues can be that the start position lies outside the map region or within the obstacle. Please try a different starting position.")
		return 

	goal_c, goal_r = map(int, raw_input("Enter goal coordinates (x y): ").split())
	goal_r = input_map.shape[0] - goal_r
	if (goal_r < 0 or goal_c < 0 or goal_r >= input_map.shape[0] or goal_c >= input_map.shape[1] or obstacles.insideObstacle(goal_r, goal_c, radius=(radius + clearance))):
		print("ERROR: This goal state is unreachable for the given robot rize and clearance distance. Possible issues can be that the goal position lies outside the map region or within the obstacle. Please try a different goal position.")
		return 

	start_time = time.clock()
	path = dijkstra.getDijkstraPath(input_map, (start_r, start_c), (goal_r, goal_c), original_map=orign_map)
	print "Time to run Dijkstra:", time.clock() - start_time, "seconds"

	# Visualize the path on the input_map
	for i in path:
		orign_map[i.current_coords] = 255
	cv2.imshow("Map", orign_map)
	
	# if 'q' is pressed then quit video
	while(1):
		key = cv2.waitKey(1) & 0xFF
		if key == 27 or key == ord("q"):
		    break

if __name__ == '__main__':
	main()
