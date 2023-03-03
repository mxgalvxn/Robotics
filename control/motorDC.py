##########
#CONTORL PID DE MOTOR DE DC

#############
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

import math
import control  

######################
#Parametros del motor
Bm = 0.001 #Coeficiente de friccion viscosa
Bl = 0.001 #Coeficiente de friccion de la carga
Jl = 0.01 #Momento de inercia de la carga
Jm = 0.0078 #Momento de inercia del motor
km = 0.83 #Constante del motor
kb = 0.83 #Constante de la fuerza electromotriz del motor
La = 0.88*(1e-3) #Inductancia de armadura del motor
Ra = 4.5 #Resistencia de armadura del motor
n1 = 10 #Numero de dientes del engrane 1
n2 = 50 #Numero de dientes del engrane 2 
########################
#Tiempo de simulacion
start = 0
stop = 1
step = 1e-3
time = np.arange(start, stop, step)
#####################

def f(x,t):
    dx_dt = [0,0,0]
    va = 12 #Entrada de voltaje 
    n = (n1/n2)
    BEq = Bm + pow(n,2) * Bl #Friccion equivalente
    JEq = Jm + pow(n,2) * Jl #Momento de inercia equivalente
    dx_dt[0] = x[1]
    dx_dt[1] = (-BEq/JEq) * x[1] + (km/JEq) * x[2]
    dx_dt[2] = (-kb/La) + x[1] - (Ra/La) * x[2] + (1/La) *va
    return dx_dt

######################
Sol = odeint(f, y0 = [0,0,0], time)
print(Sol)
################
#Graficas
#velocidad angular del motor
plt.plot(time, Sol [:1], 'b', label = 'x2')
plt.xlabel('t Segundos')
plt.ylabel( 'x1 rad/s')
plt.title( ' Velocidad angular')
plt.grid
