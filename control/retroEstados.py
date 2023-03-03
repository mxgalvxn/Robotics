####################################################
#Control de un Robot con Retroalimentación de Estados
#Dr. Humberto Valadez
####################################################
#Importación de Librerias
import numpy as np
import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt
####################################################
#Parametros del Robot
b = 0.01 #Fricción viscosa
lc = 0.5 #Distancia al centro de masa
l = 1 #Tamaño del brazo
m = 1 #Masa del brazo
g = 9.81 #Aceleración de la gravedad
I = (1/3)*m*pow(l,2)
####################################################
alfa1 = b*pow(lc,2)/(m*pow(lc,2)+I)
alfa0=m*g*lc/(m*pow(lc,2)+I)
gama = 1/(m*pow(lc,2)+I)
####################################################
#Ganancias del controlador
k1 = 10000
k2 = 20000
####################################################
#Vector de Tiempo de Simulación
start = 0
stop = 10
step =1e-3
t = np.arange(start,stop,step)
####################################################
#Referencia



#####################################################
def f(x,t):
    r = math.sin(t)
    dx_dt = [0,0]
    W = k1*(x[1]- math.sin(x[0])- k2*x[1])
    u = (1/gama)*(-k1*(x[0]-r)-k2*x[1]+alfa1*x[1]+alfa0*math.sin(x[0]) + W)
    dx_dt[0] = x[1]
    dx_dt[1] = -alfa1*x[1]-alfa0*math.sin(x[0])+gama*u
    return dx_dt
####################################################
#Solución de las ecuaciones diferenciales
Solucion = odeint(f, y0 =[0,0],t=t)
print('Solución', Solucion)
#Graficas
#Posición Angular del Robot
plt.plot(t,Solucion[:,0], 'b', label='x1(t)')
plt.xlabel('Tiempo (seg)')
plt.ylabel('x1(t)')
plt.title('Angulo del Robot (rad)')
plt.grid()
plt.show()

#Velocidad Angular del Robot
plt.plot(t,Solucion[:,1], 'r', label='x2(t)')
plt.xlabel('Tiempo (seg)')
plt.ylabel('x2(t)')
plt.title('Velocidad Angular del Robot (rad/s)')
plt.grid()
plt.show()
