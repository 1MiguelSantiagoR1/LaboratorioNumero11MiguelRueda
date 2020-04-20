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
-----------------------------------------------------------------------------------------------------------------------
print("GANANACIAS")
ganancias = calculador(ingresos,egresos)
imprimir(ganacias)
-----------------------------------------------------------------------------------------------------------------
punto g  
import numpy as np
elementos2 = np.random.randint(0,400+1 , size = 48).reshape(4,12)
def mejor_ciudad(elementos2):
    ciudades = np.array(["Bucaramanga","Floridablanca","giron","Pidecuesta"])
    
    suma = np.array([
        [np.sum(elementos2[0])],
        [np.sum(elementos2[1])],
        [np.sum(elementos2[2])],
        [np.sum(elementos2[3])],
        ])
    if suma[0] > suma[1] and suma[0] > suma[2] and suma[0] > suma[3]:
        print("La ciudad {} tiene los valores con mayores ganancias, con total de :{}".format(ciudades[0], suma[0]))
    elif suma[1] > suma[0] and suma[1] > suma[2] and suma[1] > suma[3]:
        print("La ciudad {}  tiene los valores con mayores ganancias, con un total de :{}".format(ciudades[1], suma[1]))
    elif suma[2] > suma[0] and suma[2] > suma[1] and suma[2] > suma[3]:
        print("La ciudad {}  tiene los valores con mayores ganancias, con un total de :{}".format(ciudades[2], suma[2]))
    else:
        print("La ciudad {}  tiene los valores con mayores ganancias, con un total de :{}".format(ciudades[3], suma[3]))

mejorciudad = mejor_ciudad(elementos2)
----------------------------------------------------------------------------------------------------------------------------------------
punto h
import numpy as np
elementos2 = np.random.randint(0,400+1 , size = 48).reshape(4,12)
def peor_ciudad(elementos):
    ciudades = np.array(["Bucaramanga","Floridablanca","giron","Pidecuesta"])
    
    suma = np.array([
        [np.sum(elementos[0])],
        [np.sum(elementos[1])],
        [np.sum(elementos[2])],
        [np.sum(elementos[3])],
        ])
    if suma[0] < suma[1] and suma[0] < suma[2] and suma[0] < suma[3]:
        print("La ciudad {} tiene los valores con menores ganancias, con total de :{}".format(ciudades[0], suma[0]))
    elif suma[1] < suma[0] and suma[1] < suma[2] and suma[1] < suma[3]:
        print("La ciudad {}  tiene los valores con menores ganancias, con un total de :{}".format(ciudades[1], suma[1]))
    elif suma[2] < suma[0] and suma[2] < suma[1] and suma[2] < suma[3]:
        print("La ciudad {}  tiene los valores con menores ganancias, con un total de :{}".format(ciudades[2], suma[2]))
    else:
        print("La ciudad {}  tiene los valores con menores ganancias, con un total de :{}".format(ciudades[3], suma[3]))

mejorciudad = mejor_ciudad(elementos2)
---------------------------------------------------------------------------------------------------------------------------------------
punto i  
import numpy as np
elementos2 = np.random.randint(0,400 , size = 48).reshape(4,12)
def mejor_ciudad(elementos2):
    meses = np.array(["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"])
    ciudades = np.array(["Bucaramanga","Floridablanca","giron","Pidecuesta"])
    
    for i in range(0,4,1):
        maximo = np.argmax(elementos2[i])
        print("El mes {} para la ciudad {} sus ganacias fueron de {} en millones de pesos".format(meses[maximo],ciudades[i],elementos2[i][maximo]))

mejorciudad = mejor_ciudad(elementos2)
print("")
------------------------------------------------------------------------------------------------------------------------------------------------------
#Parte 2 
#Punto a

import numpy as np
from random import randint, uniform,random
#Primero se crea el array de los personajes con sus stats ordenados dependiendo de la clase.
personajes_stats = np.array([
  #1. Orden en = Fuerza,Destreza,Constitucion,Inteligencia,Sabiduria y Carisma

  #BARBAROS
  [
  #Se ordena con el np.sort con un orden de menor a mayor y luego lo invertiremos con [::-1]Y asi atribuir los valores mas altos a los atributos de estilo Fisico
   [np.sort(np.random.randint(10,19, size = 6))[::-1]],
   [np.sort(np.random.randint(10,19, size = 6))[::-1]],
   [np.sort(np.random.randint(10,19, size = 6))[::-1]]
  ],

  #Clèrigo
  [
    [np.sort(np.random.randint(10,19, size = 6))],
    [np.sort(np.random.randint(10,19, size = 6))],
    [np.sort(np.random.randint(10,19, size = 6))]
  ],
  
  #Guerrero
  [
    [np.sort(np.random.randint(10,19, size = 6))[::-1]],
    [np.sort(np.random.randint(10,19, size = 6))[::-1]],
    [np.sort(np.random.randint(10,19, size = 6))[::-1]]
  ],

  #Bardo
  [
    [np.sort(np.random.randint(10,19, size = 6))],
    [np.sort(np.random.randint(10,19, size = 6))],
    [np.sort(np.random.randint(10,19, size = 6))]
  ],

  #Paladin
  [
    [np.sort(np.random.randint(10,19, size = 6))[::-1]],
    [np.sort(np.random.randint(10,19, size = 6))[::-1]],
    [np.sort(np.random.randint(10,19, size = 6))[::-1]]
  ],

  #Druida
  [
    [np.sort(np.random.randint(10,19, size = 6))],
    [np.sort(np.random.randint(10,19, size = 6))],
    [np.sort(np.random.randint(10,19, size = 6))]
  ],
  
  #Picaro 
   [
    [np.sort(np.random.randint(10,19, size = 6))[::-1]],
    [np.sort(np.random.randint(10,19, size = 6))[::-1]],
    [np.sort(np.random.randint(10,19, size = 6))[::-1]]
  ],

  #Mago
  [
    [np.sort(np.random.randint(10,19, size = 6))],
    [np.sort(np.random.randint(10,19, size = 6))],
    [np.sort(np.random.randint(10,19, size = 6))]
  ]])

-----------------------------------------------------------------------------------------------------------------------------------------
Parte 2
punto b
import numpy as np
from random import randint, uniform,random
#Primero se crea el array de los personajes con sus stats ordenados dependiendo de la clase.
personajes_stats = np.array([
  #1. Orden en = Fuerza,Destreza,Constitucion,Inteligencia,Sabiduria y Carisma

  #BARBAROS
  [
  #Se ordena con el np.sort con un orden de menor a mayor y luego lo invertiremos con [::-1]Y asi atribuir los valores mas altos a los atributos de estilo Fisico
   [np.sort(np.random.randint(10,19, size = 6))[::-1]],
   [np.sort(np.random.randint(10,19, size = 6))],
   [np.sort(np.random.randint(10,19, size = 6))[::-1]],
   [np.sort(np.random.randint(10,19, size = 6))],
   [np.sort(np.random.randint(10,19, size = 6))[::-1]],
   [np.sort(np.random.randint(10,19, size = 6))]

  ],

  #Clèrigo
  [
    [np.sort(np.random.randint(10,19, size = 6))],
    [np.sort(np.random.randint(10,19, size = 6))],
    [np.sort(np.random.randint(10,19, size = 6))]
  ],
  
  #Guerrero
  [
    [np.sort(np.random.randint(10,19, size = 6))[::-1]],
    [np.sort(np.random.randint(10,19, size = 6))[::-1]],
    [np.sort(np.random.randint(10,19, size = 6))[::-1]]
  ],

  #Bardo
  [
    [np.sort(np.random.randint(10,19, size = 6))],
    [np.sort(np.random.randint(10,19, size = 6))],
    [np.sort(np.random.randint(10,19, size = 6))]
  ],

  #Paladin
  [
    [np.sort(np.random.randint(10,19, size = 6))[::-1]],
    [np.sort(np.random.randint(10,19, size = 6))[::-1]],
    [np.sort(np.random.randint(10,19, size = 6))[::-1]]
  ],

  #Druida
  [
    [np.sort(np.random.randint(10,19, size = 6))],
    [np.sort(np.random.randint(10,19, size = 6))],
    [np.sort(np.random.randint(10,19, size = 6))]
  ],
  
  #Picaro 
   [
    [np.sort(np.random.randint(10,19, size = 6))[::-1]],
    [np.sort(np.random.randint(10,19, size = 6))[::-1]],
    [np.sort(np.random.randint(10,19, size = 6))[::-1]]
  ],

  #Mago
  [
    [np.sort(np.random.randint(10,19, size = 6))],
    [np.sort(np.random.randint(10,19, size = 6))],
    [np.sort(np.random.randint(10,19, size = 6))]
  ]])
clases = np.array(["Barbaros","Paladin","Mago","Picaro","Guerrero","Druida"])
jugadores = input("Digite la cantidad de jugadores (Max 3) : ")
import random
clase1 = random.choice(clases)
clase2 = random.choice(clases)
clase3 = random.choice(clases)
personajes = personajes_stats[0][0]
personajes2 = personajes_stats[1][0]
personajes3 = personajes_stats[2][0]
personajes4 = personajes_stats[3][0]
personajes5 = personajes_stats[4][0]
personajes6 = personajes_stats[5][0]


if jugadores == "1":
  print("La clase escojida es :",clase1)
  if clase1 == "Barbaros":
    print("Y sus atributos son: ")
    print("FUE = ", personajes[0][0])
    print("DES = ", personajes[0][1])
    print("CON = ", personajes[0][2])
    print("INT = ", personajes[0][3])
    print("SAB = ", personajes[0][4])
    print("CAR = ", personajes[0][5])
  if clase1 == "Paladin":
    print("Y sus atributos son: ")
    print("FUE = ", personajes[0][0])
    print("DES = ", personajes[0][1])
    print("CON = ", personajes[0][2])
    print("INT = ", personajes[0][3])
    print("SAB = ", personajes[0][4])
    print("CAR = ", personajes[0][5])
  if clase1 == "Guerrero":
    print("Y sus atributos son: ")
    print("FUE = ", personajes[0][0])
    print("DES = ", personajes[0][1])
    print("CON = ", personajes[0][2])
    print("INT = ", personajes[0][3])
    print("SAB = ", personajes[0][4])
    print("CAR = ", personajes[0][5])
  if clase1 == "Mago":
    print("Y sus atributos son: ")
    print("FUE = ", personajes2[0][0])
    print("DES = ", personajes2[0][1])
    print("CON = ", personajes2[0][2])
    print("INT = ", personajes2[0][3])
    print("SAB = ", personajes2[0][4])
    print("CAR = ", personajes2[0][5])
  if clase1 == "Picaro":
    print("Y sus atributos son: ")
    print("FUE = ", personajes2[0][0])
    print("DES = ", personajes2[0][1])
    print("CON = ", personajes2[0][2])
    print("INT = ", personajes2[0][3])
    print("SAB = ", personajes2[0][4])
    print("CAR = ", personajes2[0][5])
  if clase1 == "Druida":
    print("Y sus atributos son: ")
    print("FUE = ", personajes2[0][0])
    print("DES = ", personajes2[0][1])
    print("CON = ", personajes2[0][2])
    print("INT = ", personajes2[0][3])
    print("SAB = ", personajes2[0][4])
    print("CAR = ", personajes2[0][5])
if jugadores == "2":
  print("La clase escojida para el jugador 1 es :",clase1)
  if clase1 == "Barbaros":
    print("Y sus atributos son: ")
    print("FUE = ", personajes[0][0])
    print("DES = ", personajes[0][1])
    print("CON = ", personajes[0][2])
    print("INT = ", personajes[0][3])
    print("SAB = ", personajes[0][4])
    print("CAR = ", personajes[0][5])
  if clase1 == "Paladin":
    print("Y sus atributos son: ")
    print("FUE = ", personajes[0][0])
    print("DES = ", personajes[0][1])
    print("CON = ", personajes[0][2])
    print("INT = ", personajes[0][3])
    print("SAB = ", personajes[0][4])
    print("CAR = ", personajes[0][5])
  if clase1 == "Guerrero":
    print("Y sus atributos son: ")
    print("FUE = ", personajes[0][0])
    print("DES = ", personajes[0][1])
    print("CON = ", personajes[0][2])
    print("INT = ", personajes[0][3])
    print("SAB = ", personajes[0][4])
    print("CAR = ", personajes[0][5])
  if clase1 == "Mago":
    print("Y sus atributos son: ")
    print("FUE = ", personajes2[0][0])
    print("DES = ", personajes2[0][1])
    print("CON = ", personajes2[0][2])
    print("INT = ", personajes2[0][3])
    print("SAB = ", personajes2[0][4])
    print("CAR = ", personajes2[0][5])
  if clase1 == "Picaro":
    print("Y sus atributos son: ")
    print("FUE = ", personajes2[0][0])
    print("DES = ", personajes2[0][1])
    print("CON = ", personajes2[0][2])
    print("INT = ", personajes2[0][3])
    print("SAB = ", personajes2[0][4])
    print("CAR = ", personajes2[0][5])
  if clase1 == "Druida":
    print("Y sus atributos son: ")
    print("FUE = ", personajes2[0][0])
    print("DES = ", personajes2[0][1])
    print("CON = ", personajes2[0][2])
    print("INT = ", personajes2[0][3])
    print("SAB = ", personajes2[0][4])
    print("CAR = ", personajes2[0][5])
  print("La clase escojida para el jugador 2 es :",clase2)
  if clase1 == "Barbaros":
    print("Y sus atributos son: ")
    print("FUE = ", personajes3[0][0])
    print("DES = ", personajes3[0][1])
    print("CON = ", personajes3[0][2])
    print("INT = ", personajes3[0][3])
    print("SAB = ", personajes3[0][4])
    print("CAR = ", personajes3[0][5])
  if clase1 == "Paladin":
    print("Y sus atributos son: ")
    print("FUE = ", personajes3[0][0])
    print("DES = ", personajes3[0][1])
    print("CON = ", personajes3[0][2])
    print("INT = ", personajes3[0][3])
    print("SAB = ", personajes3[0][4])
    print("CAR = ", personajes3[0][5])
  if clase1 == "Guerrero":
    print("Y sus atributos son: ")
    print("FUE = ", personajes3[0][0])
    print("DES = ", personajes3[0][1])
    print("CON = ", personajes3[0][2])
    print("INT = ", personajes3[0][3])
    print("SAB = ", personajes3[0][4])
    print("CAR = ", personajes3[0][5])
  if clase1 == "Mago":
    print("Y sus atributos son: ")
    print("FUE = ", personajes4[0][0])
    print("DES = ", personajes4[0][1])
    print("CON = ", personajes4[0][2])
    print("INT = ", personajes4[0][3])
    print("SAB = ", personajes4[0][4])
    print("CAR = ", personajes4[0][5])
  if clase1 == "Picaro":
    print("Y sus atributos son: ")
    print("FUE = ", personajes4[0][0])
    print("DES = ", personajes4[0][1])
    print("CON = ", personajes4[0][2])
    print("INT = ", personajes4[0][3])
    print("SAB = ", personajes4[0][4])
    print("CAR = ", personajes4[0][5])
  if clase1 == "Druida":
    print("Y sus atributos son: ")
    print("FUE = ", personajes4[0][0])
    print("DES = ", personajes4[0][1])
    print("CON = ", personajes4[0][2])
    print("INT = ", personajes4[0][3])
    print("SAB = ", personajes4[0][4])
    print("CAR = ", personajes4[0][5])
if jugadores == "3":
  print("La clase escojida para el jugador 1 es :",clase1)
  if clase1 == "Barbaros":
    print("Y sus atributos son: ")
    print("FUE = ", personajes[0][0])
    print("DES = ", personajes[0][1])
    print("CON = ", personajes[0][2])
    print("INT = ", personajes[0][3])
    print("SAB = ", personajes[0][4])
    print("CAR = ", personajes[0][5])
  if clase1 == "Paladin":
    print("Y sus atributos son: ")
    print("FUE = ", personajes[0][0])
    print("DES = ", personajes[0][1])
    print("CON = ", personajes[0][2])
    print("INT = ", personajes[0][3])
    print("SAB = ", personajes[0][4])
    print("CAR = ", personajes[0][5])
  if clase1 == "Guerrero":
    print("Y sus atributos son: ")
    print("FUE = ", personajes[0][0])
    print("DES = ", personajes[0][1])
    print("CON = ", personajes[0][2])
    print("INT = ", personajes[0][3])
    print("SAB = ", personajes[0][4])
    print("CAR = ", personajes[0][5])
  if clase1 == "Mago":
    print("Y sus atributos son: ")
    print("FUE = ", personajes2[0][0])
    print("DES = ", personajes2[0][1])
    print("CON = ", personajes2[0][2])
    print("INT = ", personajes2[0][3])
    print("SAB = ", personajes2[0][4])
    print("CAR = ", personajes2[0][5])
  if clase1 == "Picaro":
    print("Y sus atributos son: ")
    print("FUE = ", personajes2[0][0])
    print("DES = ", personajes2[0][1])
    print("CON = ", personajes2[0][2])
    print("INT = ", personajes2[0][3])
    print("SAB = ", personajes2[0][4])
    print("CAR = ", personajes2[0][5])
  if clase1 == "Druida":
    print("Y sus atributos son: ")
    print("FUE = ", personajes2[0][0])
    print("DES = ", personajes2[0][1])
    print("CON = ", personajes2[0][2])
    print("INT = ", personajes2[0][3])
    print("SAB = ", personajes2[0][4])
    print("CAR = ", personajes2[0][5])
  print("La clase escojida para el jugador 2 es :",clase1)
  if clase1 == "Barbaros":
    print("Y sus atributos son: ")
    print("FUE = ", personajes3[0][0])
    print("DES = ", personajes3[0][1])
    print("CON = ", personajes3[0][2])
    print("INT = ", personajes3[0][3])
    print("SAB = ", personajes3[0][4])
    print("CAR = ", personajes3[0][5])
  if clase1 == "Paladin":
    print("Y sus atributos son: ")
    print("FUE = ", personajes3[0][0])
    print("DES = ", personajes3[0][1])
    print("CON = ", personajes3[0][2])
    print("INT = ", personajes3[0][3])
    print("SAB = ", personajes3[0][4])
    print("CAR = ", personajes3[0][5])
  if clase1 == "Guerrero":
    print("Y sus atributos son: ")
    print("FUE = ", personajes3[0][0])
    print("DES = ", personajes3[0][1])
    print("CON = ", personajes3[0][2])
    print("INT = ", personajes3[0][3])
    print("SAB = ", personajes3[0][4])
    print("CAR = ", personajes3[0][5])
  if clase1 == "Mago":
    print("Y sus atributos son: ")
    print("FUE = ", personajes4[0][0])
    print("DES = ", personajes4[0][1])
    print("CON = ", personajes4[0][2])
    print("INT = ", personajes4[0][3])
    print("SAB = ", personajes4[0][4])
    print("CAR = ", personajes4[0][5])
  if clase1 == "Picaro":
    print("Y sus atributos son: ")
    print("FUE = ", personajes4[0][0])
    print("DES = ", personajes4[0][1])
    print("CON = ", personajes4[0][2])
    print("INT = ", personajes4[0][3])
    print("SAB = ", personajes4[0][4])
    print("CAR = ", personajes4[0][5])
  if clase1 == "Druida":
    print("Y sus atributos son: ")
    print("FUE = ", personajes4[0][0])
    print("DES = ", personajes4[0][1])
    print("CON = ", personajes4[0][2])
    print("INT = ", personajes4[0][3])
    print("SAB = ", personajes4[0][4])
    print("CAR = ", personajes4[0][5])
  print("La clase escojida para el jugador 3 es :",clase3)
  if clase1 == "Barbaros":
    print("Y sus atributos son: ")
    print("FUE = ", personajes5[0][0])
    print("DES = ", personajes5[0][1])
    print("CON = ", personajes5[0][2])
    print("INT = ", personajes5[0][3])
    print("SAB = ", personajes5[0][4])
    print("CAR = ", personajes5[0][5])
  if clase1 == "Paladin":
    print("Y sus atributos son: ")
    print("FUE = ", personajes5[0][0])
    print("DES = ", personajes5[0][1])
    print("CON = ", personajes5[0][2])
    print("INT = ", personajes5[0][3])
    print("SAB = ", personajes5[0][4])
    print("CAR = ", personajes5[0][5])
  if clase1 == "Guerrero":
    print("Y sus atributos son: ")
    print("FUE = ", personajes5[0][0])
    print("DES = ", personajes5[0][1])
    print("CON = ", personajes5[0][2])
    print("INT = ", personajes5[0][3])
    print("SAB = ", personajes5[0][4])
    print("CAR = ", personajes5[0][5])
  if clase1 == "Mago":
    print("Y sus atributos son: ")
    print("FUE = ", personajes6[0][0])
    print("DES = ", personajes6[0][1])
    print("CON = ", personajes6[0][2])
    print("INT = ", personajes6[0][3])
    print("SAB = ", personajes6[0][4])
    print("CAR = ", personajes6[0][5])
  if clase1 == "Picaro":
    print("Y sus atributos son: ")
    print("FUE = ", personajes6[0][0])
    print("DES = ", personajes6[0][1])
    print("CON = ", personajes6[0][2])
    print("INT = ", personajes6[0][3])
    print("SAB = ", personajes6[0][4])
    print("CAR = ", personajes6[0][5])
  if clase1 == "Druida":
    print("Y sus atributos son: ")
    print("FUE = ", personajes6[0][0])
    print("DES = ", personajes6[0][1])
    print("CON = ", personajes6[0][2])
    print("INT = ", personajes6[0][3])
    print("SAB = ", personajes6[0][4])
    print("CAR = ", personajes6[0][5])
  
  
   

 

   
   
















