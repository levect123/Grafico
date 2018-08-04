from pylab import *
import matplotlib.pyplot as plt
import numpy as np
lista1 = [11,10,9]
lista2 = [8,7,6]
lista3 = [5,4,3,]

plt.xlabel("abscisa")
plt.ylabel("ordenada")
plt.plot(lista1, marker="x", linestyle=':', color='b', label = "Enero")
plt.plot(lista2, marker='*', linestyle='-', color='g', label = "Febrero")
plt.plot(lista3, marker='o', linestyle='--', color='r', label = "Marzo")
title("Graficos")
plt.legend(loc="upper right")
plt.show()
