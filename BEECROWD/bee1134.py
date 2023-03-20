tipo_combustivel = int(input())
gasolina = []
alcool = []
diesel = []

if tipo_combustivel == 1:
    alcool.append(tipo_combustivel)
elif tipo_combustivel == 2:
    gasolina.append(tipo_combustivel)
elif tipo_combustivel == 3:
    diesel.append(tipo_combustivel)

while tipo_combustivel != 4:
    tipo_combustivel = int(input())

    if tipo_combustivel == 1:
        alcool.append(tipo_combustivel)
    elif tipo_combustivel == 2:
        gasolina.append(tipo_combustivel)
    elif tipo_combustivel == 3:
        diesel.append(tipo_combustivel)

print(f'MUITO OBRIGADO')
print(f'Alcool: {len(alcool)}')
print(f'Gasolina: {len(gasolina)}')
print(f'Diesel: {len(diesel)}')