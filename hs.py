import numpy as np
import pandas as pd

def calcula_presiones(cantidad_columnas,cantidad_rendijas,matrix_presiones,iteraciones):

    for num_columna in range(cantidad_columnas):
       if num_columna == 0:
           for num_fila in range(cantidad_rendijas):
               matrix_presiones[num_columna][num_fila] = valor_presion_entrada
       if num_columna == (cantidad_columnas - 1):
           for num_fila in range(cantidad_rendijas):
               matrix_presiones[num_columna][num_fila] = valor_presion_salida

       for num_iteracion in range(iteraciones): 
            if num_columna > 0:
                if num_columna < cantidad_columnas - 1:
                    for num_fila in range(cantidad_rendijas):
                        if num_fila == 0:
                            if num_iteracion == 0:
                                matrix_presiones[num_columna][num_fila] = 0
                            elif num_iteracion > 0:
                                matrix_presiones[num_columna][num_fila]=matrix_presiones[num_columna][num_fila+1]
                            else:
                                matrix_presiones[num_columna][num_fila] = matrix_presiones[num_columna][num_fila+1]
                        elif num_fila == cantidad_rendijas - 1:
                            matrix_presiones[num_columna][num_fila] = matrix_presiones[num_columna][num_fila-1]
                        else:
                            matrix_presiones[num_columna][num_fila] = (matrix_presiones[num_columna][num_fila-1] + matrix_presiones[num_columna-1][num_fila]+matrix_presiones[num_columna][num_fila+1]+matrix_presiones[num_columna+1][num_fila])/4

    np.set_printoptions(precision=4)
    np.set_printoptions(suppress=True)
    print(pd.DataFrame(matrix_presiones))

if __name__ == "__main__":

  #cantidad de rendijas del aparato de helle shaw 
  cantidad_rendijas = 14
  # valor de la presion de entrada del aparato de helle shaw
  valor_presion_entrada = 5
  # valor de la presion de salida del aparato de helle shaw
  valor_presion_salida = 2
  # cantidad de divisiones en la cuales se va a medir las presiones o velocidades
  cantidad_columnas = 10
  # longitud total del aparato de helle shaw
  longitud_helle = 1000
  # matrix inicial donde se calcularan las presiones
  matrix_presiones = np.zeros(shape=(cantidad_columnas,cantidad_rendijas)) 
  # cantidad de iteraciones para que los valores
  iteraciones = 3
  calcula_presiones(cantidad_columnas,cantidad_rendijas,matrix_presiones,iteraciones)  
  #calcula_velocidades()


