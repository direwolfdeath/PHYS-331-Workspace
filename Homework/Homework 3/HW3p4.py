import numpy as np										#Import necessary libraries
import matplotlib.pyplot as plt
from copy import deepcopy

def newtonRaphsonMOD(f,df,a,b):
	fa = f(a)
	if fa == 0.0: return a
	fb = f(b)
	if fb == 0.0: return b
	if np.sign(fa) == np.sign(fb): 
		print('Root is not bracketed')
		return []
	x = 0.5*(a + b)                    
	sigma_array=[]
	for i in range(30):
		fx = f(x)
		# Try a Newton-Raphson step    
		dfx = df(x)
		# If division by zero, push x out of bounds
		try: dx = -fx/dfx
		except ZeroDivisionError: dx = b - a
		xNew= deepcopy(x) + dx							#Modification to find difference between iters
		sigma_array.append(abs(x-xNew))
		x = deepcopy(xNew)
	x_iter_vals=np.arange(1,(len(sigma_array)+1))		#Graph of error as a function of iteration,							
	np.asarray(sigma_array)								#used a log scale to best display the steep
	plt.scatter(x_iter_vals,sigma_array)					#dropoff in error.
	plt.axhline(color='black')
	plt.axvline(color='black')
	plt.grid()
	plt.xlim(0,8)
	plt.xlabel('Iterations')
	plt.ylabel('Error')
	plt.title('Problem 4: Error as a Function of Iteration')
	plt.yscale('log')
	plt.ylim(1e-10,1e2)
	plt.show()
	return sigma_array

def f1(x):                                         	#The function that we are analyzing
    return (x+10)*(x-25)*(np.power(x,2)+45)
def f1_prime(x):									#The derivative of the above function
    return 4*np.power(x,3)-45*np.power(x,2)-410*x-675

f, df, a, b = f1, f1_prime, 0, 40
newtonRaphsonMOD(f,df,a,b)					#Running the Newton-Raphson program for the desired function