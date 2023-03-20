salario = float(input())
percentual = 0

if 0 <= salario <= 400:
    percentual = 0.15
elif 400 < salario <= 800:
    percentual = 0.12
elif 800 < salario <= 1200:
    percentual = 0.10
elif 1200 < salario <= 2000:
    percentual = 0.07
else:
    percentual = 0.04

novo_salario = salario * (1 + percentual)
reajuste_ganho = novo_salario - salario

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste_ganho:.2f}')
print(f'Em percentual: {percentual * 100:.0f} %')
