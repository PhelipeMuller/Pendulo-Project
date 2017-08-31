import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint

m = 3 #Massa do Pendulo(Kg)
l = 2 #Tamano do barbante(m)
g = 9.8 # Aceleração da Gravidade



x0 = 0
vx0 = 0
y0 = 0
vy0 = 0
Y0 = [x0,vx0,y0,vy0]

def SistemaEqs(Y, t):
	x = Y[0]
	vx = Y[1]
	y = Y[2]
	vy = Y[3]
	
	dxdt = vx
	dvxdt = (m*g-(m*g*math.cos(Theta)-m*w**2*l)*math.sin(Theta)/m)
	dydt = vy
	dvydt = ((m*g*Math.cos(Theta)-m*w**2*l)*math.sin(Theta)/m)

	return [dxdt,dvxdt,dydt,dvydt]

sol = odeint(SistemaEqs,Y0, T)

plt.plot(sol[:,0],sol[:,2])
plt.show()