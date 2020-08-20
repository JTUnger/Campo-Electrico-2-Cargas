import numpy as np
import matplotlib
import math 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# caracteristicas cargas
# Q1
q1 = 1.5
q1_xpos = 1
q1_ypos = 3
# Q2
q2 = -1
q2_xpos = -1 
q2_ypos = -2

# crear grid con limites x0, x1 : y0, y1
x0 = -5
x1 = 5
y0 = -5
y1 = 5
x = np.arange(x0, x1, 0.2)
y = np.arange(y0, y1, 0.2)
X,Y = np.meshgrid(x,y)

# Ex y Ey en funcion de Grid X, Y y la pos de ambas cargas
Ex = (q1*(X - q1_xpos))/ ((X - q1_xpos)**2 + (Y - q1_ypos)**2) + (q2*(X - q2_xpos))/ ((X - q2_xpos)**2 + (Y - q2_ypos)**2)
Ey = (q1*(Y - q1_ypos))/ ((X - q1_xpos)**2 + (Y - q1_ypos)**2) + (q2*(Y - q2_ypos))/ ((X - q2_xpos)**2 + (Y - q2_ypos)**2)

# plotear el streamplot y las cargas puntuales (Rojo = Carga Positiva) (Azul = Carga Negativa)
plt.streamplot(X, Y , Ex, Ey, color = "y")
if q1 > 0:
    plt.plot(q1_xpos,q1_ypos, "or")
if q1 < 0:
    plt.plot(q1_xpos,q1_ypos, "ob")
if q2 > 0:
    plt.plot(q2_xpos,q2_ypos, "or")
if q2 < 0:
    plt.plot(q2_xpos,q2_ypos, "ob")

# titulo y lables del plot
plt.title("Campo generado por 2 cargas puntuales")
plt.xlabel("x")
plt.ylabel("y")
red = mpatches.Patch(color = "red", label = "Pos")
blue = mpatches.Patch(color = "blue", label = "Neg")
plt.legend(handles = [red,blue])

plt.show()

