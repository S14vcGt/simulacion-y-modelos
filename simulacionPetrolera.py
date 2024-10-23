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
#print ((300000 * 150) * 0.4)
import random as rd
chance = rd.randint(1,100)

if chance <= 40:
    pass