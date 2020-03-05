class Node(object):
	
	##
	## Constructs a new instance.
	##
	## :param      current_coords:  The current coordinates
	## :type       current_coords:  (row, col)
	## :param      parent_coords:   The parent coordinates
	## :type       parent_coords:   (row, col)
	## :param      movement_cost:   Movement cost from start node to current node
	## :type       movement_cost:   float
	## :param      goal_cost:       The goal cost
	## :type       goal_cost:       float
	##
	def __init__(self, 
				 current_coords, 
				 parent_coords, 
				 movement_cost, 
				 goal_cost):
		self.current_coords = current_coords
		self.parent_coords = parent_coords
		self.movement_cost = movement_cost
		self.goal_cost = goal_cost

	##
	## Match all attributes of the current object with the random_node
	##
	## :param      random_node:  The node to match the current object with
	## :type       random_node:  Node
	##
	## :returns:   True if all the attributes match, False otherwise
	## :rtype:     boolean
	##
	def deepMatch(self, random_node):
		return (self.current_coords == random_node.current_coords and
				self.parent_coords == random_node.parent_coords and
				self.movement_cost == random_node.movement_cost and
				self.goal_cost == random_node.goal_cost)

	
	##
	## Match only the current_coords attributes of the current object with the random_node
	##
	## :param      random_node:  The node to match the current object with
	## :type       random_node:  Node
	##
	## :returns:   True if current_coords attribute matches, False otherwise
	## :rtype:     boolean
	##
	def shallowMatch(self, random_node):
		return (self.current_coords == random_node.current_coords)


	##
	## Prints all the information regarding the current configuration.
	##
	def printNode(self):
		print("current_coords:\t", current_coords)
		print("parent_coords:\t", parent_coords)
		print("movement_cost:\t", movement_cost)
		print("goal_cost:\t", goal_cost)
