N = int(input())
saidas = []
for i in range(N):
    valor = int(input())
    if valor % 2 == 0 and valor > 0:
        saida = 'EVEN POSITIVE'
    elif valor % 2 != 0 and valor > 0:
        saida = 'ODD POSITIVE'
    elif valor % 2 == 0 and valor < 0:
        saida = 'EVEN NEGATIVE'
    elif valor % 2 != 0 and valor < 0:
        saida = 'ODD NEGATIVE'
    else: 
        saida = 'NULL'
    saidas.append(saida)
for i in saidas:
    print(i)