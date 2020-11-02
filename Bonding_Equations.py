
import numpy as np
import matplotlib.pyplot as plt
from math import pi

epsilon = 8.854 * (10**(-12))
constant = 1 / ((4*3.1415*epsilon))
firstCharge = 1
secondCharge = 1

electPotList=[]
electForceList=[]
distance = np.linspace(1, 100, 10001)
for i in distance:
	electricPotential = (1 / (constant))*(firstCharge / (distance**2))
	electPotList.append(electricPotential)
	electrostaticForce = electricPotential * secondCharge
	electForceList.append(electrostaticForce)




#electrostaticForce = (firstCharge * secondCharge)/(distance ** 2)
electricPotential = (1 / (constant))*(firstCharge / (distance**2))
electrostaticForce = electricPotential * secondCharge

#plt.plot(xdata, ydata, 'ob:', label = "Data")
def main():
	plt.grid()
	plt.xlabel('X')
	plt.ylabel('Y')
	distance = np.linspace(1, 100, 10001)
	ytheory = electricPotential
	y2theory = electrostaticForce
	plt.plot(distance, ytheory, '-r', label = "EP")
	plt.plot(distance, y2theory, '-r', label = "EForce")
	plt.legend(loc = 'upper left')
	plt.show()
main()