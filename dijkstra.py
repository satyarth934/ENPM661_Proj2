import os
import cv2
import numpy as np
import heapq

import sys
sys.dont_write_bytecode = True

import obstacles
import node
import utils


def function(input_map):
	start_r, start_c = 10, 10
	goal_r, goal_c = 14, 14
	start_node = node.Node((start_r, start_c), None, 0, utils.euclideanDistance((start_r, start_c), (goal_r, goal_c)))
	goal_node = node.Node((goal_r, goal_c), None, -1, 0)

	# Saving a tuple with total cost and the state node
	minheap = [((start_node.movement_cost + start_node.goal_cost), start_node)]
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

	while len(minheap) > 0:
		_, curr_node = heapq.heappop(minheap)

		if curr_node.shallowMatch(goal_node):
			print("Reached Goal!")
			# backtrack to get the path
			break
		
		# if hit an obstacle, ignore this movement
		if input_map[curr_node.current_coords] != 0:
			continue

		for row_step, col_step in movement_steps:
			# Action Move
			next_node = actions.actionMove(curr_node, (goal_r, goal_c), movement_steps[0], movement_steps[1])
			
			if next_node is not None:
				# Check if the current node has already been visited.
				# If it has, then see if the current path is better than the previous one
				# based on the total cost = movement cost + goal cost
				
				if next_node.current_coords in visited_nodes:
					# if (next_node.movement_cost + next_node.goal_cost) < (visited_nodes[idx].movement_cost + visited_nodes[idx].goal_cost):
					if (next_node.movement_cost + next_node.goal_cost) < (visited_nodes[next_node.current_coords].movement_cost + visited_nodes[next_node.current_coords].goal_cost):
						visited_nodes[next_node.current_coords].movement_cost = next_node.movement_cost
						visited_nodes[next_node.current_coords].goal_cost = next_node.goal_cost
						visited_nodes[next_node.current_coords].parent = next_node.parent

						h_idx = utils.findInHeap(next_node, minheap)
						if h_idx > -1:
							minheap[idx][1].movement_cost = next_node.movement_cost
							minheap[idx][1].goal_cost = next_node.goal_cost
							minheap[idx][1].parent = next_node.parent

							minheap[idx][0] = next_node.movement_cost + next_node.goal_cost
				else:
					# visited_nodes.append(next_node)
					visited_nodes[next_node.current_coords] = next_node
					heapq.heappush(minheap, ((next_node.movement_cost+next_node.goal_cost), next_node))

		heapq.heapify(minheap)



def main():
	input_map = obstacles.getMap()
	function(input_map)


if __name__ == '__main__':
	main()