import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import *

x = linspace(0, 5, 20)

fig, ax = plt.subplots(facecolor='w', edgecolor='k')
ax.plot(x, sin(x), marker="o", color="r", linestyle='None')

ax.grid(True)
ax.set_xlabel('X') #Eje x
ax.set_ylabel('Y') #Eje y
ax.grid(True)
ax.legend(["y = x**2"])

plt.title('Puntos')
plt.show()

fig.savefig("grafica.png") #Guardando 
