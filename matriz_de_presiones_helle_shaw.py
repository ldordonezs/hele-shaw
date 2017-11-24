import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def matrismulti(filas,colll,matrizpre,iteraciones,valor_obstaculo_x,valor_obstaculo_y,valor_obstaculo_x1,valor_obstaculo_y1):

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

    Internos =(valor_presion_salida+valor_presion_entrada)*0.5
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


        numerokol = 0

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

    #print("los nodos internos tiene un valor inicial de ",Internos)

    print(pd.DataFrame(matrizpre))
    print(pd.DataFrame(matestorbo))
    print(pd.DataFrame(latotal))
    print(pd.DataFrame(peinado_matrices(latotal,iteraciones,colll,filas,valor_obstaculo_x,valor_obstaculo_y,valor_obstaculo_x1,valor_obstaculo_y1)))

    plt.imshow(peinado_matrices(latotal,iteraciones,colll,filas,valor_obstaculo_x,valor_obstaculo_y,valor_obstaculo_x1,valor_obstaculo_y1));
    plt.colorbar()
    plt.show()


def peinado_matrices(latotal,iteraciones,colll,filas,valor_obstaculo_x,valor_obstaculo_y,valor_obstaculo_x1,valor_obstaculo_y1):

    iteraciones = 0
    for num_iteracion in range(iteraciones):

        numerokol = 1
        numefil = 1

        for numerokol in range(colll-1):
            numerokol = numerokol+1
            if numerokol < colll-1:
                for numefil in range(filas-1):
                    if numefil < filas-2:
                        latotal[numefil+1][numerokol] = ((latotal[numefil+1][numerokol-1]) + (latotal[numefil+1][numerokol+1]) + (latotal[numefil+2][numerokol]) + (latotal[numefil][numerokol]))*0.25

        numerokol = 0 #el numero de fila lo vuelve a cero el for

        for numefil in range(filas-1):
            if numefil < filas-2:
                latotal[numefil+1][numerokol] = ((latotal[numefil][numerokol]) + (latotal[numefil+2][numerokol]) + (latotal[numefil+1][numerokol+1]))/3

        numerokol = colll-1

        for numefil in range(filas-1):
            if numefil < filas-2:
                latotal[numefil+1][numerokol] = ((latotal[numefil][numerokol]) + (latotal[numefil+2][numerokol]) + (latotal[numefil+1][numerokol-1]))/3

    return latotal



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
  valor_presion_entrada = 10
  # valor de la presion de salida del aparato de helle shaw
  valor_presion_salida = 2

  # longitud total del aparato de helle shaw
  longitud_helle = 7
  # matrix inicial donde se calcularan las presiones
  matrizpre = np.zeros(shape=(filas,colll))
  matestorbo= np.ones(shape=(filas,colll))
  latotal= np.ones(shape=(filas,colll))
  # cantidad de iteraciones para que los valores
  iteraciones = 500
  matrismulti(filas,colll,matrizpre,iteraciones,valor_obstaculo_x,valor_obstaculo_y,valor_obstaculo_x1,valor_obstaculo_y1)
