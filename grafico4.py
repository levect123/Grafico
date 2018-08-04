from pylab import *
import matplotlib.pyplot as plt
import numpy as np
#definimos el periodo de la graficas senoidal
periodo = 2
#definimos el array dimensional
x = np.linspace(0, 10, 1000)
#definimos la funcion senoidal
y = np.sin(2*np.pi*x/periodo)
#creamos la figura
plt.figure()
#primera grafica
plt.subplot(2,2,1)
plt.plot(x, y, "r")
#segunda grafica
plt.subplot(2,2,2)
plt.plot(x, y, "g")
#tercera grafica
plt.subplot(2,2,3)
plt.plot(x, y, "b")
#cuarta grafica
plt.subplot(2,2,4)
plt.plot(x, y, "k")
#mostramos en pantalla
plt.show()




plt.xlabel("abscisa")
plt.ylabel("ordenada")
plt.plot(lista1, marker="x", linestyle=':', color='b', label = "Enero")
plt.plot(lista2, marker='*', linestyle='-', color='g', label = "Febrero")
plt.plot(lista3, marker='o', linestyle='--', color='r', label = "Marzo")
title("Graficos")
plt.legend(loc="upper right")
plt.show()
