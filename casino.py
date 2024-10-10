import random as rd
import pandas as pd
import polars as pl

def casino(iteraciones):
    saldo = 1000
    apuesta = saldo 

    moneda = ['cara','cruz']

    historia = []

    for _ in range(iteraciones):
        dado = rd.randint(1,6)
        if rd.choice(moneda) == 'cara' and  dado % 2 == 0 :
            saldo *= 2
            apuesta = saldo / 2
            historia.append(1)
        else:
            saldo -= apuesta
            apuesta *= 2
            historia.append(0)
    
    trad = pd.DataFrame({'victorias':historia})
    polars = pl.DataFrame({'victorias':historia})

    print (f"{trad.mean()}, {trad.median()}, {trad.mode()}\n")
    print("-" for i in range(34))
    print(f"\n{polars.mean()}, {polars.median()}")
    print(f"\nsaldo: {saldo}, ultima apuesta: {apuesta}")

casino(100)