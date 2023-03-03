import numpy as np
import math as m

# Define vectors AP and AP BORG

def rotTras(theta, vect, eje, sistema):
    px = vect[0]
    py = vect[1]
    pz = vect[2]

    if eje == "x":
        RTx = np.array([[1,0,0, px],
                [0,  m.cos(theta), -m.sin(theta), py],
                [0, m.sin(theta),m.cos(theta), pz],
                [0,0,0,1]])
        print(RTx)
        print()
        return RTx *  sistema

    elif eje == "y":
        RTy = np.array([[m.cos(theta), 0, m.sin(theta), px],
                    [0 ,1 , 0, py],
                    [-m.sin(theta), 0, m.cos(theta), pz],
                    [0, 0, 0, 1]])
        return RTy * sistema
    
    else:
        RTz = np.array([[m.cos(theta), -m.sin(theta), 0, px],
                    [m.sin(theta), m.cos(theta), 0, py],
                    [0, 0, 1, pz],
                    [0, 0, 0, 1]])
        return RTz * sistema

def Rot(theta, eje):
    if eje == "x":
        Rx = np.array([[1, 0, 0 ], 
                 [0,  m.cos(theta), -m.sin(theta)],
                 [0, m.sin(theta),m.cos(theta)]])
        return Rx
    
    elif eje == "y":
        Ry = np.array([[ m.cos(theta), 0, m.sin(theta) ], 
                [0,  1, 0],
                [-m.sin(theta), 0, m.cos(theta)]])
        return Ry

    else:
        Rz = np.array([[m.cos(theta), -m.sin(theta), 0 ], 
                [m.sin(theta),  m.cos(theta), 0],
                [0, 0, 1 ]])
        return Rz


def trasRot(theta, vect, eje, sistema):
    px = vect[0]
    py = vect[1]
    pz = vect[2]

    if eje == "x":
        TRx = np.array([[1, 0, 0, px],
                [0, m.cos(theta), -m.sin(theta), py*m.cos(theta) - pz*m.sin(theta)],
                [0, m.sin(theta), m.cos(theta), py*m.sin(theta) + pz*m.cos(theta)],
                [0, 0, 0, 1 ]])
        return TRx *  sistema

    elif eje == "y":
        TRy = np.array([[m.cos(theta), 0, m.sin(theta), px * m.cos(theta) + pz * m.sin(theta)],
                [0, 1, 0, py],
                [-m.sin(theta), 0, m.cos(theta), pz * m.cos(theta) - px * m.sin(theta)],
                [0, 0, 0 ,1]])
        return TRy *  sistema
    
    else:
        TRz = np.array([[m.cos(theta), -m.sin(theta), 0, px * m.cos(theta) - py * m.sin(theta)],
                [m.sin(theta), m.cos(theta), 0, px * m.sin(theta) - py * m.cos(theta)],
                [0, 0, 1, pz],
                [0, 0, 0, 1]])
        return TRz * sistema




# BP= np.array([[-5.0],[3.0],[7.0]])
# APBORG= np.array([[2.0],[10.0],[3.0]])
# AP= BP + APBORG
# print("BP=", AP)

# print("APBORG =", APBORG)

sistema = np.array([-3,4, -11, 1])

vector = np.array([8,-4,12])

grados = m.radians(90)
RP = rotTras(grados, vector, "x", sistema)
print(RP)
