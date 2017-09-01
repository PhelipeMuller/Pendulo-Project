from scipy.integrate import odeint
import numpy as np
import math
import matplotlib.pyplot as plt


t=np.arange(0,15,0.01)



r=5
m=5
g=9.8

Y=[math.pi/3,0]



def eq(Y,t):
	teta=Y[0]
	w=Y[1]

	dtetadt=w
	dwdt=-g*math.sin(math.radians(teta))/r

	return dtetadt,dwdt



sol=odeint(eq,Y,t)
listax=[]
listay=[]
listaT=[]
for teta in sol[:,0]:
	for w in sol[:,1]:
		T=m*g*math.cos(math.radians(teta))+m*w*w*r
	listaT.append(T)

	x=math.sin(teta)*r
	y=-math.cos(teta)*r
	listax.append(x)
	listay.append(y)




plt.plot(listax,listay)
plt.axis("equal")
plt.show()