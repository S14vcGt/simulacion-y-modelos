# Hacer el programa de la exploración petrolera. 40% es la probabilidad de encontrar petróleo, si se encuentra,
# 40% va al estado y 60% a la empresa si es que se, si no se encuentra, se pierde inversión de la exploración
''' 
¿Que estrategia conviene?

umbral de éxito 

La exploración cuesta 1M$

Si se encuentra hay 300mil barriles cada uno a 150$

correr las simulaciones y sacar la desviacion estandar de los resultados para ver 
si con ese 40% de probabilidad la ganancia sigue siendo de 45 millones 

'''
import random as rd
import pandas as pd
import numpy as np

corridas = 10
times = np.empty(corridas)
costo_exploracion = 1000000
ganancia_esperada = (300000*150)*.6

for i in range(corridas):
    chance = rd.randint(1, 100)
    if chance <= 40:
        times[i] = 1
    else:
        times[i] = 0

data = pd.DataFrame({"se_encontro": times})

veces_que_se_gano = (data["se_encontro"] ==1).sum()
veces_que_se_perdio = (data["se_encontro"] == 0).sum()

ganancias_reales = veces_que_se_gano * ganancia_esperada - veces_que_se_perdio * costo_exploracion

media= data.mean()["se_encontro"]

desviacion_estandar = data.std()["se_encontro"]

reporte = f'''
corridas de la simulacion: {corridas}
veces que se encontro el petroleo: {veces_que_se_gano}
veces que no se encontro nada: {veces_que_se_perdio}
ganancias netas por las expediciones exitosas: {veces_que_se_gano * ganancia_esperada}
perdidas totales de las expediciones fallidas: {veces_que_se_perdio * costo_exploracion}
ganancias totales: {ganancias_reales}
umbral de exito: {media}
desviacion estandar: {desviacion_estandar}
'''
print(reporte)
    