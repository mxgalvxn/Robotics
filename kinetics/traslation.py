import numpy as np
import matplotlib.pyplot as plt

# Parametros del robot
L1 = 10
L2 = 10
L3 = 5

# Longitud total del brazo
Ltot = L1 + L2 + L3


#a) Theta 1 from 0 to 180 degrees, for a fixed value of Theta 2.
# Plot del caso A
X1 = Ltot * np.cos(np.arange(1, 181) * np.pi / 180)
Y1 = Ltot * np.sin(np.arange(1, 181) * np.pi / 180)
plt.figure('Plot caso A')
plt.title('Plot caso A')
plt.plot(X1, Y1)
plt.xlabel('posicion en x')
plt.ylabel('posicion en y')
plt.axis('equal')

# Longitud de la segunda parte del brazo
Ltot2 = L2 + L3

#b) Theta 1 from 0 to 180 degrees AND Theta 2 from 0 to 180 degrees. Consider a subsampling of the combinatorics of those values. 
# Plot del caso B
X2 = L1 * np.cos(np.arange(1, 181) * np.pi / 180) + Ltot2 * np.cos(2 * np.arange(1, 181) * np.pi / 180)
Y2 = L1 * np.sin(np.arange(1, 181) * np.pi / 180) + Ltot2 * np.sin(2 * np.arange(1, 181) * np.pi / 180)
plt.figure('Plot caso B')
plt.title('Plot caso B')
plt.plot(X2, Y2)
plt.xlabel('posicion en x')
plt.ylabel('posicion en y')
plt.axis('equal')
plt.show()
