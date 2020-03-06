import os
import cv2
import numpy as np


def euclideanDistance(state1, state2):
	return np.sqrt(((state1[0] - state2[0]) ** 2) + ((state1[1] - state2[1]) ** 2))


##
## Finds a node in heap based on only the current coordinate values.
##
## :param      node:       The node to be searched
## :type       node:       Node
## :param      node_list:  The list of nodes where we look for the node
## :type       node_list:  List of nodes
##
## :returns:   index position of where the node is found (-1 if not found)
## :rtype:     int
##
def findInHeap(node, node_list):
	node_list_coords = [item[1].current_coords for item in node_list]
	if node.current_coords in node_list_coords:
		return node_list_coords.index(node.current_coords)
	return -1


def backtrack(node, visited_nodes):
	## printing both the arguments
	print("Node details:")
	node.printNode()
	print("Visited nodes -----")
	for key in visited_nodes:
		visited_nodes[key].printNode()
		print("---")


def drawOnMap(input_map, coords, visualize=False):
	# if coords[0] < 0 or coords[1] < 0:
	# 	print "input_map[", coords , "]:", input_map[coords]
	input_map[coords] = 255

	if visualize:
		cv2.imshow("exploration", input_map)
		cv2.waitKey(10)


def main():
	print(euclideanDistance((10,10), (12,12)))


if __name__ == '__main__':
	main()