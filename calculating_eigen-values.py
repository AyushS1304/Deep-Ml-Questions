# Calculate Eigenvalues of a Matrix
# Medium
# Linear Algebra


# Write a Python function that calculates the eigenvalues of a 2x2 matrix. The function should return a list containing the eigenvalues, sort values from highest to lowest.

# Example:
# Input:
# matrix = [[2, 1], [1, 2]]
# Output:
# [3.0, 1.0]
# Reasoning:
# The eigenvalues of the matrix are calculated using the characteristic equation of the matrix, which for a 2x2 matrix is 
# λ are the eigenvalues.

# Solution using the characteristic polynomial of a 2x2 matrix. The eigenvalues are calculated using the formula derived from the determinant and trace of the matrix.
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a=matrix[0][0]
	b=matrix[0][1]
	c=matrix[1][0]
	d=matrix[1][1]

	trace=a+d
	det= (a*d)-(b*c)
	discriminant= (trace * trace)- 4*det
	root=discriminant**0.5
	eigen1= (trace+root)/2
	eigen2=(trace-root)/2

	if eigen1 >=eigen2:
		eigenvalues=[float(eigen1),float(eigen2)]
	else:
		eigenvalues=[float(eigen2),float(eigen1)]
	return eigenvalues