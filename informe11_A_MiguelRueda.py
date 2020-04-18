Punto b
import numpy as np
def generador(min,max):
   x = np.random.randint(min,max , size = 48).reshape(4,12)
   return x
ingresos = generador(100,181)
egresos = generador(60,131)
print("Los ingresos son: ")
print(ingresos)
print("")
print("Los Egresos son: ")
print(egresos)

