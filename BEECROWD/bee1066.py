contador_positivo = 0
contador_negativo = 0
contador_par = 0
contador_impar = 0

for i in range(5):
    valores = int(input())

    if valores % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1
    if valores > 0:
        contador_positivo += 1
    elif valores < 0:
        contador_negativo += 1
print(f'{contador_par} valor(es) par(es)\n{contador_impar} valor(es) impar(es)\n{contador_positivo} valor(es) positivos(s)\n{contador_negativo} valor(es) negativo(s)')
