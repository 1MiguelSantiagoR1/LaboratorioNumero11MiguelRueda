Punto a
import numpy as np
def generador(min,max):
   x = np.random.randint(min,max , size = 48).reshape(4,12)
   return x
gen = generador(1,17)

print(gen)