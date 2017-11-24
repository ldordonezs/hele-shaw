import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pdb as code

def matrismulti(filas,colll,matvel,iteraciones,valor_obstaculo_x,valor_obstaculo_y,valor_obstaculo_x1,valor_obstaculo_y1):

    for valy in range(14,23):
          for valx in range(0,4):
              matestorbo[valy][valx] = 0

    for valy in range(14,23):
          for valx in range(21,25):
              matestorbo[valy][valx] = 0

    matestorbo[valor_obstaculo_x][valor_obstaculo_y] = 0
    matestorbo[valor_obstaculo_x][valor_obstaculo_y+1] = 0
    matestorbo[valor_obstaculo_x][valor_obstaculo_y-1] = 0
    matestorbo[valor_obstaculo_x-1][valor_obstaculo_y] = 0
    matestorbo[valor_obstaculo_x+1][valor_obstaculo_y] = 0

    matestorbo[valor_obstaculo_x1][valor_obstaculo_y1] = 0
    matestorbo[valor_obstaculo_x1][valor_obstaculo_y1+1] = 0
    matestorbo[valor_obstaculo_x1][valor_obstaculo_y1-1] = 0
    matestorbo[valor_obstaculo_x1-1][valor_obstaculo_y1] = 0
    matestorbo[valor_obstaculo_x1+1][valor_obstaculo_y1] = 0

    Internos =(vesal+Velin)*0.5
    for numefil in range(filas):
       if numefil == 0:
           for numerokol in range(colll):
               matvel[numefil][numerokol] = Velin        #Asignacion de valores iniciales de la matvel

       elif numefil > 0:
           for numerokol in range(colll):
               matvel[numefil][numerokol] = Internos

       if numefil == (filas - 1):                                           #los cuales son los de la parter superior e inferior del hele-shaw
           for numerokol in range(colll):                                   #son valores valvulados de la matriz de presiones
               matvel[numefil][numerokol] = vesal

    for num_iteracion in range(iteraciones):

        numerokol = 1
        numefil = 1

        for numerokol in range(colll-1):
            numerokol = numerokol+1
            if numerokol < colll-1:

                for numefil in range(filas-1):
                    if numefil < filas-2:
                        matvel[numefil+1][numerokol] = ((matvel[numefil+1][numerokol-1]) + (matvel[numefil+1][numerokol+1]) + (matvel[numefil+2][numerokol]) + (matvel[numefil][numerokol]))*0.25


        numerokol = 0

        for numefil in range(filas-1):
            if numefil < filas-2:
                matvel[numefil+1][numerokol] = ((matvel[numefil][numerokol]) + (matvel[numefil+2][numerokol]) + (matvel[numefil+1][numerokol+1]))/3

        numerokol = colll-1

        for numefil in range(filas-1):
            if numefil < filas-2:
                matvel[numefil+1][numerokol] = ((matvel[numefil][numerokol]) + (matvel[numefil+2][numerokol]) + (matvel[numefil+1][numerokol-1]))/3


    matveltotal= matvel*matestorbo

    np.set_printoptions(precision=4)
    np.set_printoptions(suppress=True)

    #print("los nodos internos tiene un valor inicial de ",Internos)

    print(pd.DataFrame(matvel))
    print(pd.DataFrame(matestorbo))
    print(pd.DataFrame(matveltotal))
    print(pd.DataFrame(correccion(matveltotal,iteraciones,colll,filas,valor_obstaculo_x,valor_obstaculo_y,valor_obstaculo_x1,valor_obstaculo_y1)))

    plt.imshow(correccion(matveltotal,iteraciones,colll,filas,valor_obstaculo_x,valor_obstaculo_y,valor_obstaculo_x1,valor_obstaculo_y1));
    plt.colorbar()
    plt.show()


def correccion(matveltotal,iteraciones,colll,filas,valor_obstaculo_x,valor_obstaculo_y,valor_obstaculo_x1,valor_obstaculo_y1):

    iteraciones = 0
    for num_iteracion in range(iteraciones):

        numerokol = 1
        numefil = 1

        for numerokol in range(colll-1):
            numerokol = numerokol+1
            if numerokol < colll-1:
                for numefil in range(filas-1):
                    if numefil < filas-2:
                        matveltotal[numefil+1][numerokol] = ((matveltotal[numefil+1][numerokol-1]) + (matveltotal[numefil+1][numerokol+1]) + (matveltotal[numefil+2][numerokol]) + (matveltotal[numefil][numerokol]))*0.25

        numerokol = 0 #el numero de fila lo vuelve a cero el for

        for numefil in range(filas-1):
            if numefil < filas-2:
                matveltotal[numefil+1][numerokol] = ((matveltotal[numefil][numerokol]) + (matveltotal[numefil+2][numerokol]) + (matveltotal[numefil+1][numerokol+1]))/3

        numerokol = colll-1

        for numefil in range(filas-1):
            if numefil < filas-2:
                matveltotal[numefil+1][numerokol] = ((matveltotal[numefil][numerokol]) + (matveltotal[numefil+2][numerokol]) + (matveltotal[numefil+1][numerokol-1]))/3

    return matveltotal



if __name__ == "__main__":

  valor_obstaculo_y = 12
  valor_obstaculo_x = 15

  valor_obstaculo_x1 = 21
  valor_obstaculo_y1 = 12

  #cantidad de rendijas del aparato de helle shaw
  colll = 25
  # cantidad de divisiones en la cuales se va a medir las presiones o velocidades
  filas = 36
  # valor de la presion de entrada del aparato de helle shaw
  Velin = 10
  # valor de la presion de salida del aparato de helle shaw
  vesal = 2

  # longitud total del aparato de helle shaw
  longitud_helle = 7
  # matrix inicial donde se calcularan las presiones
  matvel = np.zeros(shape=(filas,colll))
  matestorbo= np.ones(shape=(filas,colll))
  matveltotal= np.ones(shape=(filas,colll))
  # cantidad de iteraciones para que los valores
  iteraciones = 10000
  matrismulti(filas,colll,matvel,iteraciones,valor_obstaculo_x,valor_obstaculo_y,valor_obstaculo_x1,valor_obstaculo_y1)
