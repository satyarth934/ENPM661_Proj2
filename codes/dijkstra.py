import os
import cv2
import copy
import numpy as np
import heapq

import sys
sys.dont_write_bytecode = True

import actions
import obstacles
import node
import utils


##
## Gets the dijkstra path.
## In this algorithm, the heuristic cost from
## current node to goal node is not considered.
##
## :param      input_map:  The input map
## :type       input_map:  { type_description }
##
def getDijkstraPath(input_map, start_pos, goal_pos, original_map, visualize=False):
	viz_map = copy.deepcopy(original_map)

	# start_r, start_c = 10, 10
	# goal_r, goal_c = 30,10
	start_r, start_c = start_pos
	goal_r, goal_c = goal_pos
	
	start_node = node.Node((start_r, start_c), None, 0, None)
	goal_node = node.Node((goal_r, goal_c), None, -1, None)

	# Saving a tuple with total cost and the state node
	minheap = [((start_node.movement_cost), start_node)]
	heapq.heapify(minheap)

	# dictionary of all the visited nodes
	visited_nodes = {}
	visited_nodes[start_node.current_coords] = start_node

	movement_steps = [[-1, -1],
					  [-1,  0],
					  [-1, +1],
					  [ 0, -1],
					  [ 0, +1],
					  [+1, -1],
					  [+1,  0],
					  [+1, +1]]

	viz_visited_coords = []

	while len(minheap) > 0:
		_, curr_node = heapq.heappop(minheap)

		if curr_node.shallowMatch(goal_node):
			print("Reached Goal!")
			# backtrack to get the path
			path = utils.backtrack(curr_node, visited_nodes)

			return (path, viz_visited_coords)

		for row_step, col_step in movement_steps:
			# Action Move
			next_node = actions.actionMove(curr_node, row_step, col_step)
			
			if next_node is not None:
				# if hit an obstacle, ignore this movement
				if input_map[next_node.current_coords] != 0:
					continue

				# Check if the current node has already been visited.
				# If it has, then see if the current path is better than the previous one
				# based on the total cost = movement cost + goal cost
				if next_node.current_coords in visited_nodes:
					if (next_node.movement_cost) < (visited_nodes[next_node.current_coords].movement_cost):
						visited_nodes[next_node.current_coords].movement_cost = next_node.movement_cost
						visited_nodes[next_node.current_coords].parent_coords = next_node.parent_coords

						h_idx = utils.findInHeap(next_node, minheap)
						if h_idx > -1:
							minheap[h_idx] = (next_node.movement_cost, next_node)
				else:
					# visited_nodes.append(next_node)
					visited_nodes[next_node.current_coords] = next_node
					heapq.heappush(minheap, ((next_node.movement_cost), next_node))

					viz_visited_coords.append(next_node.current_coords)
					if visualize:
						utils.drawOnMap(viz_map, next_node.current_coords, visualize=visualize)

		heapq.heapify(minheap)

