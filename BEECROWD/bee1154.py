N = int(input())
i = 0
soma = 0
while N > 0:
    soma = soma + N
    N = int(input())
    i += 1
media = soma / i
print(f'{media:.2f}')
