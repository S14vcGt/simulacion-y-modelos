confesar = [True, False]

delito_menor = 2
condena_acortada = 5
condena_completa = 10

def confiesa(juan, carlos):
    if juan and carlos:
        return (condena_acortada,condena_acortada)
        
    if juan and not carlos:
        return (0,condena_completa)

    if not juan and carlos:
        return ( condena_completa, 0)

    if not juan and not carlos:
        return (delito_menor,delito_menor)


for i in range (4):
    corrida = confiesa()
