import numpy as np
import pandas as pd

def matrismulti(filas,colll,matrizpre,iteraciones):

    Internos =(valor_presion_salida+valor_presion_entrada)*0.5
    toto=0
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

            if numefil > 0:
                if numefil < filas - 1:
                    for numerokol in range(colll):
                        if numerokol == 0:
                            if num_iteracion == 0:
                                for numerokol in range(colll):

                                    matrizpre[numefil][numerokol] = Internos

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
    print(Internos)
    print(toto)
if __name__ == "__main__":

  #cantidad de rendijas del aparato de helle shaw
  colll = 5
  # valor de la presion de entrada del aparato de helle shaw
  valor_presion_entrada = 100
  # valor de la presion de salida del aparato de helle shaw
  valor_presion_salida = 0.5
  # cantidad de divisiones en la cuales se va a medir las presiones o velocidades
  filas = 20
  # longitud total del aparato de helle shaw
  longitud_helle = 7
  # matrix inicial donde se calcularan las presiones
  matrizpre = np.zeros(shape=(filas,colll))
  # cantidad de iteraciones para que los valores
  iteraciones = 1
  matrismulti(filas,colll,matrizpre,iteraciones)
  #calcula_velocidades()
