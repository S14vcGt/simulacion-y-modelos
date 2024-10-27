confesar = [True, False]


def confiesa(juan, carlos):
    delito_menor = 2
    condena_acortada = 5
    condena_completa = 10

    if juan and carlos:
        print(f"Si ambos confiesan: juan = {
              condena_acortada}, carlos = {condena_acortada}")

    if juan and not carlos:
        print(f"Si solo juan confiesa: juan = {
              0}, carlos = {condena_completa}")

    if not juan and carlos:
        print(f"Si solo carlos confiesa: juan = {
              condena_completa}, carlos = {0}")

    if not juan and not carlos:
        print(f"Si ninguno confiesa: juan = {
              delito_menor}, carlos = {delito_menor}")


for i in range(2):
    for j in range(2):
        confiesa(confesar[i], confesar[j])
