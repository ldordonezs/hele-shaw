import numpy as np
import pandas as pd

def matrismulti(filas,colll,matrizpre,iteraciones):

    for numefil in range(filas):
       if numefil == 0:
           for numerokol in range(colll):
               matrizpre[numefil][numerokol] = valor_presion_entrada        #Asignacion de valores iniciales de la matrizpre
       if numefil == (filas - 1):                                           #los cuales son los de la parter superior e inferior del hele-shaw
           for numerokol in range(colll):                                   #son valores conocidos en ingresados por el usuario
               matrizpre[numefil][numerokol] = valor_presion_salida

        for num_iteracion in range(iteraciones):
            if numefil > 0:
                if numefil < filas - 1:
                    for numerokol in range(colll):
                        if numerokol == 0:
                            if num_iteracion == 0:
                          matrizpre[numefil][numerokol] = 0
                        elif num_iteracion > 0:
                          matrizpre[numefil][numerokol]=matrizpre[numefil][numerokol+1]
                        else:
                          matrizpre[numefil][numerokol] = matrizpre[numefil][numerokol+1]
                      elif numerokol == colll - 1:
                      matrizpre[numefil][numerokol] = matrizpre[numefil][numerokol-1]
                    else:
                      matrizpre[numefil][numerokol] = (matrizpre[numefil][numerokol-1] + matrizpre[numefil-1][numerokol]+matrizpre[numefil][numerokol+1]+matrizpre[numefil+1][numerokol])/4




    np.set_printoptions(precision=4)
    np.set_printoptions(suppress=True)
    print(pd.DataFrame(matrizpre))

if __name__ == "__main__":

  #cantidad de rendijas del aparato de helle shaw
  colll = 4
  # valor de la presion de entrada del aparato de helle shaw
  valor_presion_entrada = 7
  # valor de la presion de salida del aparato de helle shaw
  valor_presion_salida = 3
  # cantidad de divisiones en la cuales se va a medir las presiones o velocidades
  filas = 20
  # longitud total del aparato de helle shaw
  longitud_helle = 10
  # matrix inicial donde se calcularan las presiones
  matrizpre = np.zeros(shape=(filas,colll))
  # cantidad de iteraciones para que los valores
  iteraciones = 5
  matrismulti(filas,colll,matrizpre,iteraciones)
  #calcula_velocidades()
