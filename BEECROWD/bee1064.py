contador_positivo = 0
lista = []
for i in range(6):
    numero = float(input())

    if numero > 0:
        lista.append(numero)
        contador_positivo += 1

soma_valores = sum(lista)


print(f'{contador_positivo} valores positivos')
print(f'{soma_valores / contador_positivo:.1f}')
