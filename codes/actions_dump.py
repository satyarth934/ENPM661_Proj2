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
