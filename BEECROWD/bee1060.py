contador_positivo = 0

for i in range(6):
    numero = float(input())

    if numero > 0:

        contador_positivo += 1


print(f'{contador_positivo} valores positivos')
