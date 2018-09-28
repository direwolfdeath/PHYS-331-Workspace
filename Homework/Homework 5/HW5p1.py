import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
import scipy as sci

def F(x_vec):
	"""
	INPUT:
		x_vec: numpy array, shape=(2,1)
	OUTPUT:
		numpy array shape = (2,1). Nonlinear transformation of x_vec over the function F(z)= 2(z)^3-3+i
	"""
	x = x_vec[0,0]
	y = x_vec[1,0]
	return np.array([[2*np.power(x,3)-6*x*np.power(y,2)-3],[6*np.power(x,2)*y-2*np.power(y,3)+1]])


def Jinv(x_vec):
	"""
	INPUT:
		x_vec: numpy array, shape = (2,1)
	OUTPUT:
		numpy array shape = (2,1)
	"""
	x = x_vec[0,0]
	y = x_vec[1,0]
	a = 6*np.power(x,2)-np.power(y,2)
	b = 12*x*y
	c = sci.power(6*np.power(x,2)+6*np.power(y,2),-2)
	return np.array([[a*c,b*c],[-1*b*c,a*c]])

def rf_newtonraphson2d(F_system, Jinv_system, x_vec0, tol, maxiter):
	x_vec = x_vec0
	for i in range(0,maxiter):
		dx = matrix_mult(Jinv_system(x_vec),F_system(x_vec))
		x = F_system(x_vec)[0,0]
		y = F_system(x_vec)[1,0]
		if np.sqrt(np.power(x,2)+np.power(y,2)) <= tol:
			return x_vec 
		else:
			x_vec = np.add(deepcopy(x_vec), -1*dx)
	return "Error: Iteration limit exceeded."


def matrix_mult(m1,m2):
	(r1,c1) = m1.shape
	(r2,c2) = m2.shape
	if c1 != r2:
		return "Error, incorect matricies computed. Please reenter matricies with appropriate dimensions."
	newentry=0
	matrix_product = np.zeros((c1,c2))
	for ra in range (0,r1):
		for cb in range (0, c2):
			for ca in range(0,c1):
				newentry = 0
				for rb in range(0,r2):
					newentry += (m1[ra,rb] * m2[rb,cb])
				matrix_product[ra,cb] = newentry			
	return matrix_product

def main():
	for vec in [[[1],[0]],[[-1],[0]],[[0],[1]],[[0],[-1]],[[-1],[-1]],[[1],[1]],[[1],[-1]],[[-1],[1]],[[0],[0]]]:
		F_system, Jinv_system, x_vec0, tol, maxiter = F, Jinv, np.array(vec), 1e-5, 1000
		if type(rf_newtonraphson2d(F_system, Jinv_system, x_vec0, tol, maxiter))== str:
			print(rf_newtonraphson2d(F_system, Jinv_system, x_vec0, tol, maxiter))
		else:
			coordinates = rf_newtonraphson2d(F_system, Jinv_system, x_vec0, tol, maxiter)
			x_val = coordinates[0,0]
			y_val = coordinates[1,0]
			print("For the coordinate pair: (" + str(x_vec0[0,0]) + "," + str(x_vec0[1,0]) + ") the system converges at (" + str(x_val) + "," + str(y_val) + ")" )


main()