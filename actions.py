import numpy as np

import node
import utils


input_map_dummy = np.zeros((200, 300))


def actionMoveLeft(data, goal_position):
	if data.current_coords[1]-1 < 0:
		return None

	current_coords = (data.current_coords[0], data.current_coords[1]-1)
	parent_coords = data.current_coords
	movement_cost = data.movement_cost + 1
	goal_cost = utils.euclideanDistance(current_coords, goal_position)

	ret_val = node.Node(current_coords, parent_coords, movement_cost, goal_cost)

	return ret_val


def actionMoveRight(data, goal_position):
	if data.current_coords[1]+1 >= input_map_dummy.shape[1]:
		return None

	current_coords = (data.current_coords[0], data.current_coords[1]+1)
	parent_coords = data.current_coords
	movement_cost = data.movement_cost + 1
	goal_cost = utils.euclideanDistance(current_coords, goal_position)

	ret_val = node.Node(current_coords, parent_coords, movement_cost, goal_cost)

	return ret_val


def actionMoveUp(data, goal_position):
	if data.current_coords[0]-1 < 0:
		return None

	current_coords = (data.current_coords[0]-1, data.current_coords[1])
	parent_coords = data.current_coords
	movement_cost = data.movement_cost + 1
	goal_cost = utils.euclideanDistance(current_coords, goal_position)

	ret_val = node.Node(current_coords, parent_coords, movement_cost, goal_cost)
	
	return ret_val


def actionMoveDown(data, goal_position):
	if data.current_coords[0]+1 >= input_map_dummy.shape[0]:
		return None

	current_coords = (data.current_coords[0]+1, data.current_coords[1])
	parent_coords = data.current_coords
	movement_cost = data.movement_cost + 1
	goal_cost = utils.euclideanDistance(current_coords, goal_position)

	ret_val = node.Node(current_coords, parent_coords, movement_cost, goal_cost)
	
	return ret_val


def actionMoveTopLeft(data, goal_position):
	if data.current_coords[0]-1 < 0 and data.current_coords[1]-1 < 0:
		return None

	current_coords = (data.current_coords[0]-1, data.current_coords[1]-1)
	parent_coords = data.current_coords
	movement_cost = data.movement_cost + np.sqrt(2)
	goal_cost = utils.euclideanDistance(current_coords, goal_position)

	ret_val = node.Node(current_coords, parent_coords, movement_cost, goal_cost)

	return ret_val


def actionMoveTopRight(data, goal_position):
	if data.current_coords[0]-1 < 0 and data.current_coords[1]+1 >= input_map_dummy.shape[1]:
		return None

	current_coords = (data.current_coords[0]-1, data.current_coords[1]+1)
	parent_coords = data.current_coords
	movement_cost = data.movement_cost + np.sqrt(2)
	goal_cost = utils.euclideanDistance(current_coords, goal_position)

	ret_val = node.Node(current_coords, parent_coords, movement_cost, goal_cost)

	return ret_val


def actionMoveBottomLeft(data, goal_position):
	if data.current_coords[0]+1 >= input_map_dummy.shape[0] and data.current_coords[1]-1 < 0:
		return None

	current_coords = (data.current_coords[0]+1, data.current_coords[1]-1)
	parent_coords = data.current_coords
	movement_cost = data.movement_cost + np.sqrt(2)
	goal_cost = utils.euclideanDistance(current_coords, goal_position)

	ret_val = node.Node(current_coords, parent_coords, movement_cost, goal_cost)

	return ret_val


def actionMoveBottomRight(data, goal_position):
	if data.current_coords[0]+1 >= input_map_dummy.shape[0] and data.current_coords[1]+1 >= input_map_dummy.shape[1]:
		return None

	current_coords = (data.current_coords[0]+1, data.current_coords[1]+1)
	parent_coords = data.current_coords
	movement_cost = data.movement_cost + np.sqrt(2)
	goal_cost = utils.euclideanDistance(current_coords, goal_position)

	ret_val = node.Node(current_coords, parent_coords, movement_cost, goal_cost)

	return ret_val


def actionMove(data, goal_position, row_step, col_step):
	if ((data.current_coords[0] + row_step) < 0) and 
		((data.current_coords[0] + row_step) >= input_map_dummy.shape[0]) and 
		((data.current_coords[1] + col_step) < 0) and 
		((data.current_coords[1] + col_step) >= input_map_dummy.shape[1]):
		return None

	current_coords = (data.current_coords[0] + row_step, data.current_coords[1] + col_step)
	parent_coords = data.current_coords
	if (np.abs(row_step) + np.abs(col_step)) == 1:
		movement_cost = data.movement_cost + np.sqrt(2)
	elif (np.abs(row_step) + np.abs(col_step)) == 2:
		movement_cost = data.movement_cost + 1
	else:
		print("WRONG movement values!!")
		return None

	goal_cost = utils.euclideanDistance(current_coords, goal_position)

	ret_val = node.Node(current_coords, parent_coords, movement_cost, goal_cost)

	return ret_val