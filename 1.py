import numpy as np
import pandas as pd
print("Programa de calculo de lineas de corriente")

y = int(input("Ingrese ubicacion obstaculo en X:"))
x = int(input("Ingrese ubicacion obstaculo en Y:"))


def matrismulti(filas,colll,matrizpre,iteraciones):
    matestorbo[x][y] = 0
    matestorbo[x][y+1] = 0
    matestorbo[x][y-1] = 0
    matestorbo[x-1][y] = 0
    matestorbo[x+1][y] = 0
    Internos =(valor_presion_salida+valor_presion_entrada)*0.5
    toto = 0
    for numefil in range(filas):
       if numefil == 0:
           for numerokol in range(colll):
               matrizpre[numefil][numerokol] = valor_presion_entrada        #Asignacion de valores iniciales de la matrizpre

       elif numefil > 0:
           for numerokol in range(colll):
               matrizpre[numefil][numerokol] = Internos                     #llenado de valores internos iniciales que son el promedio enter el valor_presion_entrada y el valor_presion_salida

       if numefil == (filas - 1):                                           #los cuales son los de la parter superior e inferior del hele-shaw
           for numerokol in range(colll):                                   #son valores conocidos en ingresados por el usuario
               matrizpre[numefil][numerokol] = valor_presion_salida

    for num_iteracion in range(iteraciones):

        numerokol = 1
        numefil = 1

        for numerokol in range(colll-1):
            numerokol = numerokol+1
            if numerokol < colll-1:

                for numefil in range(filas-1):
                    if numefil < filas-2:
                        matrizpre[numefil+1][numerokol] = ((matrizpre[numefil+1][numerokol-1]) + (matrizpre[numefil+1][numerokol+1]) + (matrizpre[numefil+2][numerokol]) + (matrizpre[numefil][numerokol]))*0.25


        numerokol =0

        for numefil in range(filas-1):
            if numefil < filas-2:
                matrizpre[numefil+1][numerokol] = ((matrizpre[numefil][numerokol]) + (matrizpre[numefil+2][numerokol]) + (matrizpre[numefil+1][numerokol+1]))/3

        numerokol = colll-1

        for numefil in range(filas-1):
            if numefil < filas-2:
                matrizpre[numefil+1][numerokol] = ((matrizpre[numefil][numerokol]) + (matrizpre[numefil+2][numerokol]) + (matrizpre[numefil+1][numerokol-1]))/3


    latotal= matrizpre*matestorbo

    np.set_printoptions(precision=4)
    np.set_printoptions(suppress=True)
    print(pd.DataFrame(matrizpre))

    print("los nodos internos tiene un valor inicial de ",Internos)
    print(pd.DataFrame(matestorbo))
    print(pd.DataFrame(latotal))



if __name__ == "__main__":

  #cantidad de rendijas del aparato de helle shaw
  colll = 6
  # valor de la presion de entrada del aparato de helle shaw
  valor_presion_entrada = 10
  # valor de la presion de salida del aparato de helle shaw
  valor_presion_salida = 2
  # cantidad de divisiones en la cuales se va a medir las presiones o velocidades
  filas = 10
  # longitud total del aparato de helle shaw
  longitud_helle = 7
  # matrix inicial donde se calcularan las presiones
  matrizpre = np.zeros(shape=(filas,colll))
  matestorbo= np.ones(shape=(filas,colll))
  latotal= np.ones(shape=(filas,colll))
  # cantidad de iteraciones para que los valores
  iteraciones = 10
  matrismulti(filas,colll,matrizpre,iteraciones)
  #calcula_velocidades()
