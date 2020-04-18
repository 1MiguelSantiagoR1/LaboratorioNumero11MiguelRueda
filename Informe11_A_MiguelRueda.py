Punto a
import numpy as np
def generador(min,max):
   x = np.random.randint(min,max , size = 48).reshape(4,12)
   return x
gen = generador(1,17)
print(gen)
---------------------------------------------------------------
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
-----------------------------------------------------------------------
punto c  
import numpy as np

def imprimir():
    x = np.array([
        [100,110,178,107,155,127,106,114,130,169,127,103],
        [131,158,103,160,105,127,114,155,114,178,104,160],
        [104,127,114,153,139,150,162,137,173,150,127,114],
        [149,150,100,130,159,107,178,101,109,127,130,178],
        ])

    ciudades = np.array(["Bucaramanga","Floridablanca","giron","Pidecuesta"])
    mes = np.array(["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"])
    print("Filas --> {} <-- Columnas".format(x.shape))
    print("")

    for c in range(0,4,1):
        print("Para la ciudad {}, sus ingresos o egresos, segun sea su caso fueron de: ".format(ciudades[c]))
        for f in range(0,12,1):
              print("Para el mes {}: {}".format(mes[f],x[c][f]))
    
ing = imprimir()
------------------------------------------------------------------------------
punto D  
print("\n ARRAY INGRESOS: ")
imprimir_ingresos = imprimir(ingresos)
print("\n ARRAY EGRESOS: ")
imprimir_ingresos = imprimir(egresos)
-----------------------------------------------------------------------------------------
punto E
import numpy as np
def calculador(a,b):
    r = (np.subtract(a,b))
    return r
res1 = calculador(20,12)
print(res1)
---------------------------------------------------------------------------------
punto F   
 




