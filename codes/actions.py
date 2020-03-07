import numpy as np

import node
import utils


input_map_dummy = np.zeros((200, 300))


##
## Move from the current coordinates Node to the next valid movement.
## The values of row_step and col_step specify the direction of movement 
## from one of the 8 directions. Use of the row_step and col_step parameters
## takes away the need to specify 8 different functions for all the different movements.
##
## :param      data:           The current coordinates
## :type       data:           Node
## :param      row_step:       The row step
## :type       row_step:       int
## :param      col_step:       The col step
## :type       col_step:       int
## :param      goal_position:  The goal position. Used only for A_star, not for dijkstra.
## :type       goal_position:  (row, col)
##
## :returns:   Node for the new position in case of valid movement, None otherwise
## :rtype:     Node
##
def actionMove(data, row_step, col_step, goal_position=None):
	if ((data.current_coords[0] + row_step) < 0) or ((data.current_coords[0] + row_step) >= input_map_dummy.shape[0]) or ((data.current_coords[1] + col_step) < 0) or ((data.current_coords[1] + col_step) >= input_map_dummy.shape[1]):
		return None

	current_coords = (data.current_coords[0] + row_step, data.current_coords[1] + col_step)
	parent_coords = data.current_coords
	if (np.abs(row_step) + np.abs(col_step)) == 1:
		movement_cost = data.movement_cost + 1
	elif (np.abs(row_step) + np.abs(col_step)) == 2:
		movement_cost = data.movement_cost + np.sqrt(2)
	else:
		print("WRONG movement values!!")
		return None

	if goal_position is None:
		goal_cost = None
	else:
		goal_cost = utils.euclideanDistance(current_coords, goal_position)

	ret_val = node.Node(current_coords, parent_coords, movement_cost, goal_cost)

	return ret_val