import numpy as np

def page_rank(link_matrix, damping_factor, num_iterations):
# Check if the link matrix is square
	rows, cols = link_matrix.shape
	if rows != cols:
		raise ValueError('Link matrix must be square.')
	link_matrix = link_matrix / link_matrix.sum(axis=0, keepdims=True) #normalizes the matrix, if it is already normalized, this won't do anything
	importance_weights = np.ones(rows) / rows #creating the importance weight array, then divides it by number of rows, so like 3x3 would be 1/3 for all its values
	for i in range(num_iterations): #running the page rank algorithm
		x = (1 - damping_factor) / rows
		y = damping_factor * np.dot(link_matrix,importance_weights)
		importance_weights = x+y
	return importance_weights

	
# Example usage
link_matrix = np.array([ [0, 3,1],
[0,0,1],
[1,0,0]
])

damping_factor = 0.85
num_iterations = 100

importance_weights = page_rank(link_matrix, damping_factor, num_iterations)

print('Importance Weights:')
print(importance_weights)