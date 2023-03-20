N = int(input())
sapo = []
coelho = []
rato = []

for i in range(N):
    quantidade_cobaias, tipo_cobaia = input().split(" ")
    quantidade_cobaias = int(quantidade_cobaias)

    if tipo_cobaia == 'S':
        sapo.append(quantidade_cobaias)
    elif tipo_cobaia == 'C':
        coelho.append(quantidade_cobaias)
    else:
        rato.append(quantidade_cobaias)

soma_sapo = sum(sapo)
soma_coelho = sum(coelho)
soma_rato = sum(rato)
total = soma_sapo + soma_rato + soma_coelho

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {soma_coelho}')
print(f'Total de ratos: {soma_rato}')
print(f'Total de sapos: {soma_sapo}')
print(f'Percentual de coelhos:{soma_coelho / total * 100:.2f}')
print(f'Percentual de ratos:{soma_rato / total * 100:.2f}')
print(f'Percentual de sapos:{soma_sapo / total * 100:.2f}')