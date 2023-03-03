#Simulacion Mass-Spring System
# Fernanda Monserrat Galvan Romero
#------------------------------#
#Importacion de Librerias
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

m = 0.1 #Mass
k = 35 #Sping
B = 0.00 #Friction

#time vector    
start = 0
stop = 10
step = 1e-1
t = np.arange(start , stop, step)


#####
def f(z,t):
    F = 0
    dz_dt = [0,0]
    dz_dt[0] = z[1]
    dz_dt[1] = -(k/m)*z[0]-(B/m)*z[1]+(1/m)*F 
    return dz_dt

###########

Solucion = odeint(f, y0 = [0,0], t = t)

###############

#Graficas
plt.plot(t,Solucion[: ,0])
plt.title('Position m')
plt.xlabel('t')
plt.ylabel('x1(t)')
plt.grid()
# plt.show()



plt.plot(t,Solucion[: ,1])
plt.title('Position m')
plt.xlabel('t')
plt.ylabel('x1(t)')
plt.grid()
plt.show()
